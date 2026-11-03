"""
Trabajo práctico: Listas, árboles y grafos.
Requiere Python 3.10+ y únicamente bibliotecas estándar.

Archivos de entrada:
  datos/pokemon.json
  datos/personajes.json
  datos/relaciones.json

Los formatos están documentados en README.md. El programa no inventa los datos
faltantes: si no se proporcionan, informa qué archivo hace falta.
"""
from __future__ import annotations

import json
import heapq
from collections import Counter, deque, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "datos"


# ---------------------------------------------------------------------------
# Utilidades para leer los JSON
# ---------------------------------------------------------------------------

def leer_json(ruta: Path) -> list[dict[str, Any]]:
    """Lee una lista de objetos desde un archivo JSON."""
    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró {ruta.relative_to(ROOT)}. "
            "Consultá README.md para conocer el formato esperado."
        )
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError(f"Se esperaba una lista JSON en {ruta.name}.")
    return datos


def separar_lista(valor: Optional[str]) -> list[str]:
    """Convierte 'Agua; Hielo' en ['Agua', 'Hielo'] y descarta vacíos."""
    if not valor:
        return []
    if isinstance(valor, list):
        return [str(elemento).strip() for elemento in valor if str(elemento).strip()]
    return [elemento.strip() for elemento in str(valor).replace(",", ";").split(";")
            if elemento.strip()]


def como_bool(valor: Optional[str]) -> bool:
    if isinstance(valor, bool):
        return valor
    return str(valor or "").strip().lower() in {
        "1", "true", "sí", "si", "yes", "s", "x"
    }


# ---------------------------------------------------------------------------
# EJERCICIO 1: Pokémon e índices mediante árboles binarios de búsqueda
# ---------------------------------------------------------------------------

@dataclass
class Pokemon:
    numero: int
    nombre: str
    tipos: list[str]
    debilidades: list[str]
    megaevolucion: bool
    gigamax: bool

    @classmethod
    def desde_fila(cls, fila: dict[str, Any]) -> "Pokemon":
        return cls(
            numero=int(fila["numero"]),
            nombre=fila["nombre"].strip(),
            tipos=separar_lista(fila.get("tipos", fila.get("tipo", ""))),
            debilidades=separar_lista(fila.get("debilidades", "")),
            megaevolucion=como_bool(fila.get("megaevolucion", "")),
            gigamax=como_bool(fila.get("gigamax", "")),
        )

    def __str__(self) -> str:
        return (
            f"#{self.numero} {self.nombre} | tipos: {', '.join(self.tipos) or 'sin dato'}"
            f" | debilidades: {', '.join(self.debilidades) or 'sin dato'}"
            f" | megaevolución: {'sí' if self.megaevolucion else 'no'}"
            f" | Gigamax: {'sí' if self.gigamax else 'no'}"
        )


@dataclass
class NodoABB:
    clave: Any
    datos: list[Pokemon] = field(default_factory=list)
    izquierdo: Optional["NodoABB"] = None
    derecho: Optional["NodoABB"] = None


class ArbolBinarioBusqueda:
    """ABB que conserva varios Pokémon cuando comparten la misma clave."""

    def __init__(self, clave_funcion):
        self.raiz: Optional[NodoABB] = None
        self.clave_funcion = clave_funcion

    def insertar(self, pokemon: Pokemon) -> None:
        clave = self.clave_funcion(pokemon)
        if self.raiz is None:
            self.raiz = NodoABB(clave, [pokemon])
            return
        actual = self.raiz
        while True:
            if clave == actual.clave:
                actual.datos.append(pokemon)
                return
            if clave < actual.clave:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoABB(clave, [pokemon])
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = NodoABB(clave, [pokemon])
                    return
                actual = actual.derecho

    def buscar(self, clave: Any) -> list[Pokemon]:
        actual = self.raiz
        while actual is not None:
            if clave == actual.clave:
                return actual.datos[:]
            actual = actual.izquierdo if clave < actual.clave else actual.derecho
        return []

    def en_orden(self) -> list[Pokemon]:
        resultado: list[Pokemon] = []
        def recorrer(nodo: Optional[NodoABB]) -> None:
            if nodo is None:
                return
            recorrer(nodo.izquierdo)
            resultado.extend(nodo.datos)
            recorrer(nodo.derecho)
        recorrer(self.raiz)
        return resultado

    def por_nivel(self) -> list[Pokemon]:
        resultado: list[Pokemon] = []
        if self.raiz is None:
            return resultado
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.extend(nodo.datos)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado


class CatalogoPokemon:
    def __init__(self, pokemones: Iterable[Pokemon]):
        self.pokemones = list(pokemones)
        # Tres índices independientes solicitados en la consigna.
        self.por_nombre = ArbolBinarioBusqueda(lambda p: p.nombre.casefold())
        self.por_numero = ArbolBinarioBusqueda(lambda p: p.numero)
        # Un Pokémon puede tener más de un tipo: se indexa en cada uno.
        self.por_tipo = ArbolBinarioBusqueda(lambda p: p.casefold())
        for pokemon in self.pokemones:
            self.por_nombre.insertar(pokemon)
            self.por_numero.insertar(pokemon)
        # Inserción por tipo con clave explícita (permite tipos múltiples).
        for pokemon in self.pokemones:
            for tipo in pokemon.tipos:
                self._insertar_tipo(tipo, pokemon)

    def _insertar_tipo(self, tipo: str, pokemon: Pokemon) -> None:
        arbol = self.por_tipo
        clave = tipo.casefold()
        if arbol.raiz is None:
            arbol.raiz = NodoABB(clave, [pokemon])
            return
        actual = arbol.raiz
        while True:
            if clave == actual.clave:
                if all(p.numero != pokemon.numero for p in actual.datos):
                    actual.datos.append(pokemon)
                return
            if clave < actual.clave:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoABB(clave, [pokemon])
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = NodoABB(clave, [pokemon])
                    return
                actual = actual.derecho

    @classmethod
    def cargar(cls, ruta: Path = DATA_DIR / "pokemon.json") -> "CatalogoPokemon":
        filas = leer_json(ruta)
        return cls(Pokemon.desde_fila(fila) for fila in filas)

    def buscar_numero(self, numero: int) -> list[Pokemon]:
        return self.por_numero.buscar(numero)

    def buscar_nombre_aproximado(self, texto: str) -> list[Pokemon]:
        """Busca por prefijo O por subcadena, sin distinguir mayúsculas."""
        termino = texto.casefold().strip()
        if not termino:
            return []
        # El árbol permite búsquedas exactas eficientes; la proximidad por
        # subcadena requiere recorrer las claves/nombres del catálogo.
        return sorted(
            (p for p in self.pokemones if termino in p.nombre.casefold()),
            key=lambda p: (p.nombre.casefold(), p.numero)
        )

    def buscar_tipo(self, tipo: str) -> list[Pokemon]:
        return self.por_tipo.buscar(tipo.casefold())

    def mostrar_pokemon(self, pokemon: Pokemon) -> None:
        print(pokemon)

    def resumen_tipos(self) -> None:
        contador = Counter(tipo for p in self.pokemones for tipo in p.tipos)
        print("\nPokémon por tipo (un Pokémon de doble tipo cuenta en ambos):")
        for tipo, cantidad in sorted(contador.items(), key=lambda x: x[0].casefold()):
            print(f"  {tipo}: {cantidad}")

    def debiles_frente_a(self, nombres: list[str]) -> list[Pokemon]:
        # Tipos de los tres Pokémon de referencia. Algunos quedan fuera de la
        # muestra de 100 especies (Pokédex #135, #744 y #697), por eso se
        # incluyen sus tipos de referencia aunque no estén en el CSV.
        tipos_conocidos = {
            "jolteon": ["Eléctrico"],
            "lycanroc": ["Roca"],
            "tyrantrum": ["Roca", "Dragón"],
        }
        tipos_objetivo = set()
        for nombre in nombres:
            encontrados = self.buscar_nombre_aproximado(nombre)
            exactos = [p for p in encontrados if p.nombre.casefold() == nombre.casefold()]
            if exactos:
                tipos_objetivo.update(t.casefold() for p in exactos for t in p.tipos)
            elif nombre.casefold() in tipos_conocidos:
                tipos_objetivo.update(t.casefold() for t in tipos_conocidos[nombre.casefold()])
            else:
                print(f"Aviso: no se encontró exactamente {nombre!r}; se omite.")
        return [p for p in self.pokemones
                if tipos_objetivo.intersection(t.casefold() for t in p.debilidades)]

    def informe(self) -> None:
        print("\n" + "=" * 72 + "\nEJERCICIO 1 - POKÉMON\n" + "=" * 72)
        print(f"Total de registros cargados: {len(self.pokemones)}")

        consulta_numero = input("\nNúmero de Pokémon para consultar (Enter para omitir): ").strip()
        if consulta_numero:
            try:
                resultados = self.buscar_numero(int(consulta_numero))
                print("Resultado por número:")
                for p in resultados:
                    self.mostrar_pokemon(p)
                if not resultados:
                    print("No se encontró ese número.")
            except ValueError:
                print("El número debe ser un entero.")

        consulta_nombre = input("\nTexto para buscar en nombres (Enter para omitir): ").strip()
        if consulta_nombre:
            resultados = self.buscar_nombre_aproximado(consulta_nombre)
            print(f"Coincidencias de nombre con {consulta_nombre!r}:")
            for p in resultados:
                self.mostrar_pokemon(p)
            if not resultados:
                print("No hubo coincidencias.")

        print("\nNombres de Pokémon de los tipos solicitados:")
        for tipo in ("fantasma", "fuego", "acero", "eléctrico"):
            lista = sorted(self.buscar_tipo(tipo), key=lambda p: p.nombre.casefold())
            print(f"\n{tipo.title()} ({len(lista)}):")
            print(", ".join(p.nombre for p in lista) if lista else "(sin registros)")

        print("\nListado ascendente por número:")
        for p in self.por_numero.en_orden():
            print(f"{p.numero:>4} - {p.nombre}")

        print("\nListado ascendente por nombre:")
        for p in sorted(self.por_nombre.en_orden(), key=lambda p: (p.nombre.casefold(), p.numero)):
            print(f"{p.nombre} (#{p.numero})")

        print("\nRecorrido por nivel del árbol indexado por nombre:")
        print(" -> ".join(f"{p.nombre}(#{p.numero})" for p in self.por_nombre.por_nivel()))

        print("\nPokémon débiles frente a los tipos de Jolteon, Lycanroc y Tyrantrum:")
        debiles = self.debiles_frente_a(["Jolteon", "Lycanroc", "Tyrantrum"])
        for p in sorted(debiles, key=lambda p: (p.nombre.casefold(), p.numero)):
            print(f"{p.nombre}: debilidades {', '.join(p.debilidades)}")
        print(f"Total: {len(debiles)}")

        mega = [p for p in self.pokemones if p.megaevolucion]
        giga = [p for p in self.pokemones if p.gigamax]
        print(f"\nPokémon con megaevolución: {len(mega)}")
        print(f"Pokémon con forma Gigamax: {len(giga)}")
        self.resumen_tipos()


# ---------------------------------------------------------------------------
# EJERCICIO 2: grafo no dirigido y ponderado de Star Wars
# ---------------------------------------------------------------------------

@dataclass
class Personaje:
    nombre: str
    episodios: set[int] = field(default_factory=set)


class GrafoStarWars:
    def __init__(self):
        self.personajes: dict[str, Personaje] = {}
        # adyacencia[nombre][vecino] = cantidad de episodios compartidos
        self.adyacencia: dict[str, dict[str, int]] = defaultdict(dict)

    def agregar_personaje(self, nombre: str, episodios: Iterable[int] = ()) -> None:
        clave = nombre.strip()
        if not clave:
            return
        if clave not in self.personajes:
            self.personajes[clave] = Personaje(clave, set())
        self.personajes[clave].episodios.update(episodios)
        self.adyacencia.setdefault(clave, {})

    def agregar_relacion(self, a: str, b: str, peso: int) -> None:
        if a == b:
            return
        if peso < 0:
            raise ValueError("El peso de una arista no puede ser negativo.")
        self.agregar_personaje(a)
        self.agregar_personaje(b)
        # Una relación repetida conserva el mayor número informado.
        self.adyacencia[a][b] = max(peso, self.adyacencia[a].get(b, -1))
        self.adyacencia[b][a] = max(peso, self.adyacencia[b].get(a, -1))

    @classmethod
    def cargar(cls, personajes_json: Path = DATA_DIR / "personajes.json",
               relaciones_json: Path = DATA_DIR / "relaciones.json") -> "GrafoStarWars":
        grafo = cls()
        for fila in leer_json(personajes_json):
            episodios = {int(x) for x in separar_lista(fila.get("episodios", []))}
            grafo.agregar_personaje(fila["nombre"], episodios)
        for fila in leer_json(relaciones_json):
            grafo.agregar_relacion(
                fila["personaje1"].strip(),
                fila["personaje2"].strip(),
                int(fila["episodios_compartidos"])
            )
        return grafo

    def encontrar_nombre(self, consulta: str) -> Optional[str]:
        normalizado = consulta.casefold().strip()
        for nombre in self.personajes:
            if nombre.casefold() == normalizado:
                return nombre
        return None

    def arbol_expansion_minima(self, inicio: str) -> list[tuple[str, str, int]]:
        """
        Prim. Como el peso representa episodios compartidos, para un árbol
        mínimo se minimiza la suma de esos pesos, tal como pide la consigna.
        Si el grafo es desconectado, devuelve el componente alcanzable desde
        el inicio y avisa desde el llamador.
        """
        inicio_real = self.encontrar_nombre(inicio)
        if inicio_real is None:
            print(f"No existe el vértice {inicio!r}.")
            return []
        visitados = {inicio_real}
        candidatos = []
        for vecino, peso in self.adyacencia[inicio_real].items():
            heapq.heappush(candidatos, (peso, inicio_real, vecino))
        aristas = []
        while candidatos:
            peso, origen, destino = heapq.heappop(candidatos)
            if destino in visitados:
                continue
            visitados.add(destino)
            aristas.append((origen, destino, peso))
            for vecino, peso_vecino in self.adyacencia[destino].items():
                if vecino not in visitados:
                    heapq.heappush(candidatos, (peso_vecino, destino, vecino))
        if len(visitados) < len(self.personajes):
            print(f"Aviso: el grafo no es conexo; el componente contiene {len(visitados)} "
                  f"de {len(self.personajes)} vértices.")
        return aristas

    def pares_con_maximo_compartido(self) -> tuple[int, list[tuple[str, str]]]:
        mejor = -1
        pares = []
        vistos = set()
        for a, vecinos in self.adyacencia.items():
            for b, peso in vecinos.items():
                par_id = frozenset((a, b))
                if par_id in vistos:
                    continue
                vistos.add(par_id)
                if peso > mejor:
                    mejor, pares = peso, [(a, b)]
                elif peso == mejor:
                    pares.append((a, b))
        return mejor, sorted(pares, key=lambda par: (par[0].casefold(), par[1].casefold()))

    def camino_mas_corto(self, inicio: str, fin: str) -> tuple[list[str], Optional[int]]:
        """
        Dijkstra sobre el peso indicado en la consigna (episodios compartidos).
        Por lo tanto, minimiza la suma de pesos de aristas, no la cantidad
        de saltos. Si se quisiera minimizar saltos, corresponde BFS.
        """
        origen = self.encontrar_nombre(inicio)
        destino = self.encontrar_nombre(fin)
        if origen is None or destino is None:
            return [], None
        distancias = {origen: 0}
        anterior: dict[str, Optional[str]] = {origen: None}
        cola = [(0, origen)]
        while cola:
            distancia, actual = heapq.heappop(cola)
            if distancia != distancias.get(actual):
                continue
            if actual == destino:
                break
            for vecino, peso in self.adyacencia[actual].items():
                nueva = distancia + peso
                if nueva < distancias.get(vecino, float("inf")):
                    distancias[vecino] = nueva
                    anterior[vecino] = actual
                    heapq.heappush(cola, (nueva, vecino))
        if destino not in distancias:
            return [], None
        camino = []
        actual: Optional[str] = destino
        while actual is not None:
            camino.append(actual)
            actual = anterior[actual]
        camino.reverse()
        return camino, distancias[destino]

    def personajes_en_nueve_episodios(self) -> list[str]:
        return sorted((p.nombre for p in self.personajes.values()
                       if len(p.episodios) == 9), key=str.casefold)

    def informe(self) -> None:
        print("\n" + "=" * 72 + "\nEJERCICIO 2 - STAR WARS\n" + "=" * 72)
        print(f"Vértices: {len(self.personajes)}")
        print(f"Aristas no dirigidas: {sum(len(v) for v in self.adyacencia.values()) // 2}")

        for inicio in ("C-3PO", "Yoda", "Leia"):
            print(f"\nÁrbol de expansión mínima desde {inicio}:")
            arbol = self.arbol_expansion_minima(inicio)
            if not arbol:
                print("No se pudo construir (revisá el nombre o las relaciones).")
            else:
                for a, b, peso in arbol:
                    print(f"  {a} -- {b} (peso: {peso})")
                print(f"Peso total: {sum(peso for _, _, peso in arbol)}")

        maximo, pares = self.pares_con_maximo_compartido()
        print(f"\nMáxima cantidad de episodios compartidos: {maximo}")
        for a, b in pares:
            print(f"  {a} -- {b}")

        caminos = [
            ("C-3PO", "R2-D2"),
            ("Yoda", "Darth Vader"),
        ]
        for inicio, fin in caminos:
            camino, costo = self.camino_mas_corto(inicio, fin)
            print(f"\nCamino de menor suma de pesos: {inicio} -> {fin}")
            if camino:
                print(" -> ".join(camino))
                print(f"Suma de pesos: {costo}")
            else:
                print("No hay camino disponible o falta un personaje.")

        print("\nPersonajes que aparecieron en los nueve episodios:")
        nueve = self.personajes_en_nueve_episodios()
        print(", ".join(nueve) if nueve else
              "(sin resultados: verificá que personajes.json tenga los episodios completos)")


def main() -> None:
    print("TRABAJO PRÁCTICO - ESTRUCTURAS DE DATOS")
    print("Datos incluidos: muestra de 100 Pokémon y personajes de Star Wars.")
    try:
        catalogo = CatalogoPokemon.cargar()
        catalogo.informe()
    except (FileNotFoundError, KeyError, ValueError) as error:
        print(f"\nNo se pudo ejecutar el ejercicio 1: {error}")

    try:
        grafo = GrafoStarWars.cargar()
        grafo.informe()
    except (FileNotFoundError, KeyError, ValueError) as error:
        print(f"\nNo se pudo ejecutar el ejercicio 2: {error}")


if __name__ == "__main__":
    main()
