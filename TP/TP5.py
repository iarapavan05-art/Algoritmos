# Ejercicio 5 - Árbol

class NodoArbol:
    def __init__(self, nombre, es_heroe=True):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True = Héroe, False = Villano
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe=True):
        def _insertar(nodo, nombre, es_heroe):
            if nodo is None:
                return NodoArbol(nombre, es_heroe)
            if nombre.lower() < nodo.nombre.lower():
                nodo.izq = _insertar(nodo.izq, nombre, es_heroe)
            else:
                nodo.der = _insertar(nodo.der, nombre, es_heroe)
            return nodo

        self.raiz = _insertar(self.raiz, nombre, es_heroe)

    def eliminar(self, nombre):
        def _eliminar(nodo, nombre):
            if nodo is None:
                return nodo, None
            if nombre.lower() < nodo.nombre.lower():
                nodo.izq, eliminado = _eliminar(nodo.izq, nombre)
            elif nombre.lower() > nodo.nombre.lower():
                nodo.der, eliminado = _eliminar(nodo.der, nombre)
            else:
                eliminado = nodo
                if nodo.izq is None:
                    return nodo.der, eliminado
                elif nodo.der is None:
                    return nodo.izq, eliminado
                else:
                    # Sucesor inorden (mínimo del subárbol derecho)
                    sucesor = nodo.der
                    while sucesor.izq is not None:
                        sucesor = sucesor.izq
                    nodo.nombre = sucesor.nombre
                    nodo.es_heroe = sucesor.es_heroe
                    nodo.der, _ = _eliminar(nodo.der, sucesor.nombre)
            return nodo, eliminado

        self.raiz, nodo_eliminado = _eliminar(self.raiz, nombre)
        return nodo_eliminado

    def busqueda_proximidad(self, cadena):
        coincidencias = []

        def _proximidad(nodo):
            if nodo is not None:
                _proximidad(nodo.izq)
                if cadena.lower() in nodo.nombre.lower():
                    coincidencias.append(nodo)
                _proximidad(nodo.der)

        _proximidad(self.raiz)
        return coincidencias



def punto_b_listar_villanos_alfabeticamente(arbol):
    print("b. Villanos ordenados alfabéticamente:")
    def _inorden_villanos(nodo):
        if nodo is not None:
            _inorden_villanos(nodo.izq)
            if not nodo.es_heroe:
                print(f"   - {nodo.nombre}")
            _inorden_villanos(nodo.der)

    _inorden_villanos(arbol.raiz)


def punto_c_superheroes_empiezan_con_c(arbol):
    print("c. Superhéroes que empiezan con la letra 'C':")
    def _inorden_c(nodo):
        if nodo is not None:
            _inorden_c(nodo.izq)
            if nodo.es_heroe and nodo.nombre.upper().startswith('C'):
                print(f"   - {nodo.nombre}")
            _inorden_c(nodo.der)

    _inorden_c(arbol.raiz)


def punto_d_contar_superheroes(arbol):
    def _contar(nodo):
        if nodo is None:
            return 0
        actual = 1 if nodo.es_heroe else 0
        return actual + _contar(nodo.izq) + _contar(nodo.der)

    total = _contar(arbol.raiz)
    print(f"d. Cantidad total de superhéroes en el árbol: {total}")
    return total


def punto_e_modificar_dr_strange(arbol):
    print("e. Búsqueda por proximidad para corregir el nombre de Doctor Strange:")
    cadena_busqueda = "Doctor Str"
    coincidencias = arbol.busqueda_proximidad(cadena_busqueda)
    
    if coincidencias:
        for nodo_encontrado in coincidencias:
            nombre_incorrecto = nodo_encontrado.nombre
            es_heroe = nodo_encontrado.es_heroe
            print(f"   -> Encontrado personaje mal cargado: '{nombre_incorrecto}'")
            
            # Se elimina el nodo antiguo y se reinserta con el nombre corregido para mantener las propiedades del ABB
            arbol.eliminar(nombre_incorrecto)
            nombre_corregido = "Doctor Strange"
            arbol.insertar(nombre_corregido, es_heroe)
            print(f"   -> Nombre corregido exitosamente a: '{nombre_corregido}'")
    else:
        print("   -> No se encontró ningún personaje con esa aproximación.")


def punto_f_listar_superheroes_descendente(arbol):
    print("f. Superhéroes ordenados de manera descendente:")
    def _postorden_inverso(nodo):
        if nodo is not None:
            _postorden_inverso(nodo.der)
            if nodo.es_heroe:
                print(f"{nodo.nombre}")
            _postorden_inverso(nodo.izq)

    _postorden_inverso(arbol.raiz)


def punto_g_generar_bosque_y_procesar(arbol_principal):
    print("g. Generar bosque (árbol de superhéroes y árbol de villanos):")
    arbol_heroes = ArbolBinario()
    arbol_villanos = ArbolBinario()

    def _separar(nodo):
        if nodo is not None:
            _separar(nodo.izq)
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            _separar(nodo.der)

    _separar(arbol_principal.raiz)

    def _contar_nodos(nodo):
        if nodo is None:
            return 0
        return 1 + _contar_nodos(nodo.izq) + _contar_nodos(nodo.der)

    def _barrido_alfabetico(nodo):
        if nodo is not None:
            _barrido_alfabetico(nodo.izq)
            tipo = "Héroe" if nodo.es_heroe else "Villano"
            print(f"{nodo.nombre} ({tipo})")
            _barrido_alfabetico(nodo.der)

    # 1. Determinar cuántos nodos tiene cada árbol
    cant_heroes = _contar_nodos(arbol_heroes.raiz)
    cant_villanos = _contar_nodos(arbol_villanos.raiz)

    print(f"   1. Cantidad de nodos en el árbol de Superhéroes: {cant_heroes}")
    print(f"   1. Cantidad de nodos en el árbol de Villanos: {cant_villanos}")

    # 2. Realizar un barrido ordenado alfabéticamente de cada árbol
    print("\n   2. Barrido ordenado alfabéticamente del árbol de SUPERHÉROES:")
    _barrido_alfabetico(arbol_heroes.raiz)

    print("\n   2. Barrido ordenado alfabéticamente del árbol de VILLANOS:")
    _barrido_alfabetico(arbol_villanos.raiz)


def main():
    arbol_mcu = ArbolBinario()

    personajes = [
        ("Iron Man", True),
        ("Captain America", True),
        ("Captain Marvel", True),
        ("Cyclops", True),
        ("Thor", True),
        ("Spider-Man", True),
        ("Black Widow", True),
        ("Doctor Strnge", True),  # Mal cargado a propósito
        ("Hulk", True),
        ("Hawkeye", True),
        ("Thanos", False),
        ("Loki", False),
        ("Ultron", False),
        ("Hela", False),
        ("Green Goblin", False),
        ("Mysterio", False),
        ("Red Skull", False),
        ("Kang", False)
    ]

    for nombre, es_heroe in personajes:
        arbol_mcu.insertar(nombre, es_heroe)

    print(" EJERCICIO 5: ÁRBOLES - MCU (MARVEL CINEMATIC UNIVERSE)\n")

    # a. Definición del árbol con campo booleano (demostrado en la inserción inicial)
    print("a. Árbol inicial cargado con superhéroes y villanos (campo booleano es_heroe).\n")

    # b. Listar villanos ordenados alfabéticamente
    punto_b_listar_villanos_alfabeticamente(arbol_mcu)
    print()

    # c. Mostrar superhéroes que empiezan con C
    punto_c_superheroes_empiezan_con_c(arbol_mcu)
    print()

    # d. Determinar cuántos superhéroes hay en el árbol
    punto_d_contar_superheroes(arbol_mcu)
    print()

    # e. Modificar Doctor Strange usando búsqueda por proximidad
    punto_e_modificar_dr_strange(arbol_mcu)
    print()

    # f. Listar superhéroes ordenados de manera descendente
    punto_f_listar_superheroes_descendente(arbol_mcu)
    print()

    # g. Generar bosque (separar en 2 árboles: héroes y villanos) y resolver I y II
    punto_g_generar_bosque_y_procesar(arbol_mcu)


if __name__ == "__main__":
    main()









# Ejercicio 23 
from collections import deque

class NodoCriatura:
    def __init__(self, nombre, derrotado_por=None, capturada=None, descripcion=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por  
        self.capturada = capturada          
        self.descripcion = descripcion      
        self.izq = None
        self.der = None


class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None, capturada=None, descripcion=None):
        def _insertar(nodo, nombre, derrotado_por, capturada, descripcion):
            if nodo is None:
                return NodoCriatura(nombre, derrotado_por, capturada, descripcion)
            if nombre.lower() < nodo.nombre.lower():
                nodo.izq = _insertar(nodo.izq, nombre, derrotado_por, capturada, descripcion)
            elif nombre.lower() > nodo.nombre.lower():
                nodo.der = _insertar(nodo.der, nombre, derrotado_por, capturada, descripcion)
            else:
                if derrotado_por is not None:
                    nodo.derrotado_por = derrotado_por
                if capturada is not None:
                    nodo.capturada = capturada
                if descripcion is not None:
                    nodo.descripcion = descripcion
            return nodo

        self.raiz = _insertar(self.raiz, nombre, derrotado_por, capturada, descripcion)

    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if nodo is None:
                return None
            if nombre.lower() == nodo.nombre.lower():
                return nodo
            elif nombre.lower() < nodo.nombre.lower():
                return _buscar(nodo.izq, nombre)
            else:
                return _buscar(nodo.der, nombre)
        return _buscar(self.raiz, nombre)

    def eliminar(self, nombre):
        def _eliminar(nodo, nombre):
            if nodo is None:
                return nodo, None
            if nombre.lower() < nodo.nombre.lower():
                nodo.izq, eliminado = _eliminar(nodo.izq, nombre)
            elif nombre.lower() > nodo.nombre.lower():
                nodo.der, eliminado = _eliminar(nodo.der, nombre)
            else:
                eliminado = nodo
                if nodo.izq is None:
                    return nodo.der, eliminado
                elif nodo.der is None:
                    return nodo.izq, eliminado
                else:
                    sucesor = nodo.der
                    while sucesor.izq is not None:
                        sucesor = sucesor.izq
                    nodo.nombre = sucesor.nombre
                    nodo.derrotado_por = sucesor.derrotado_por
                    nodo.capturada = sucesor.capturada
                    nodo.descripcion = sucesor.descripcion
                    nodo.der, _ = _eliminar(nodo.der, sucesor.nombre)
            return nodo, eliminado

        self.raiz, nodo_eliminado = _eliminar(self.raiz, nombre)
        return nodo_eliminado

    def busqueda_coincidencia(self, cadena):
        coincidencias = []
        def _coincidencia(nodo):
            if nodo is not None:
                _coincidencia(nodo.izq)
                if cadena.lower() in nodo.nombre.lower():
                    coincidencias.append(nodo)
                _coincidencia(nodo.der)
        _coincidencia(self.raiz)
        return coincidencias

    def barrido_inorden(self):
        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.izq)
                derrotador = nodo.derrotado_por if nodo.derrotado_por else "-"
                capturador = f" | Capturada por: {nodo.capturada}" if nodo.capturada else ""
                desc = f" | Desc: {nodo.descripcion}" if nodo.descripcion else ""
                print(f"-{nodo.nombre} (Derrotado por: {derrotador}{capturador}{desc})")
                _inorden(nodo.der)
        _inorden(self.raiz)

    def barrido_por_nivel(self):
        if self.raiz is None:
            print("   El árbol está vacío.")
            return

        cola = deque([(self.raiz, 0)])
        nivel_actual = -1
        
        while cola:
            nodo, nivel = cola.popleft()
            if nivel != nivel_actual:
                nivel_actual = nivel
                print(f"\n --- Nivel {nivel_actual} ---")
            
            derrotador = nodo.derrotado_por if nodo.derrotado_por else "-"
            capturador = f" [Capturada por: {nodo.capturada}]" if nodo.capturada else ""
            print(f"   • {nodo.nombre} (Derrotado por: {derrotador}){capturador}")
            
            if nodo.izq:
                cola.append((nodo.izq, nivel + 1))
            if nodo.der:
                cola.append((nodo.der, nivel + 1))


def ejecutar_ejercicio_23():
    print("=" * 20)
    print("Ejercicio 23 - Arbol")
    print("=" * 20 + "\n")

    arbol = ArbolCriaturas()

    # Carga inicial de datos según la tabla del ejercicio
    datos_tabla = [
        ("Ceto", None),
        ("Tifón", "Zeus"),
        ("Equidna", "Argos Panoptes"),
        ("Dino", None),
        ("Pefredo", None),
        ("Enio", None),
        ("Escila", None),
        ("Caribdis", None),
        ("Euríale", None),
        ("Esteno", None),
        ("Medusa", "Perseo"),
        ("Ladón", "Heracles"),
        ("Águila del Cáucaso", None),
        ("Quimera", "Belerofonte"),
        ("Hidra de Lerna", "Heracles"),
        ("León de Nemea", "Heracles"),
        ("Esfinge", "Edipo"),
        ("Dragón de la Cólquida", None),
        ("Cerbero", None),
        ("Cerda de Cromión", "Teseo"),
        ("Ortro", "Heracles"),
        ("Toro de Creta", "Teseo"),
        ("Jabalí de Calidón", "Atalanta"),
        ("Carcinos", None),
        ("Gerión", "Heracles"),
        ("Cloto", None),
        ("Láquesis", None),
        ("Átropos", None),
        ("Minotauro de Creta", "Teseo"),
        ("Harpías", None),
        ("Argos Panoptes", "Hermes"),
        ("Aves del Estínfalo", None),
        ("Talos", "Medea"),
        ("Sirenas", None),
        ("Pitón", "Apolo"),
        ("Cierva de Cerinea", None),
        ("Basilisco", None),
        ("Jabalí de Erimanto", None),
    ]

    for nombre, derrotado in datos_tabla:
        arbol.insertar(nombre, derrotado_por=derrotado)

    # a. Listado inorden de las criaturas y quienes las derrotaron
    print("a. Listado inorden de las criaturas y quienes la derrotaron:")
    arbol.barrido_inorden()
    print()

    # b. Permitir cargar una breve descripción sobre cada criatura
    print("b. Cargar una breve descripción sobre una criatura:")
    talos_desc = "Autómata gigante de bronce creado por Hefesto para proteger la isla de Creta de invasores."
    nodo_talos = arbol.buscar("Talos")
    if nodo_talos:
        nodo_talos.descripcion = talos_desc
        print(f"   -> Se cargó exitosamente la descripción para '{nodo_talos.nombre}': '{talos_desc}'")
    print()

    # c. Mostrar toda la información de la criatura Talos
    print("c. Mostrar toda la información de la criatura Talos:")
    nodo_talos = arbol.buscar("Talos")
    if nodo_talos:
        print(f"Nombre: {nodo_talos.nombre}")
        print(f"Derrotado por: {nodo_talos.derrotado_por if nodo_talos.derrotado_por else 'Nadie'}")
        print(f"Capturada por: {nodo_talos.capturada if nodo_talos.capturada else 'Nadie'}")
        print(f"Descripción: {nodo_talos.descripcion if nodo_talos.descripcion else 'Sin descripción'}")
    print()

    # g. Cada nodo tiene el campo 'capturada' (ya integrado en la clase NodoCriatura)

    # h. Modifique los nodos de Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
    print("h. Modificar nodos (Cerbero, Toro de Creta, Cierva Cerinea, Jabalí de Erimanto) indicando que Heracles las atrapó:")
    atrapadas_por_heracles = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
    for nombre_crip in atrapadas_por_heracles:
        nodo = arbol.buscar(nombre_crip)
        if not nodo:
            # Si difiere la redacción (ej. 'Cierva Cerinea' vs 'Cierva de Cerinea')
            coincidencias = arbol.busqueda_coincidencia("Cerinea") if "Cerinea" in nombre_crip else []
            if coincidencias:
                nodo = coincidencias[0]
        
        if nodo:
            nodo.capturada = "Heracles"
            print(f"->'{nodo.nombre}' marcada como capturada por Heracles.")
        else:
            print(f"-> No se encontró el nodo para '{nombre_crip}'.")
    print()

    # j. Eliminar al Basilisco y a las Sirenas
    print("j. Eliminar al Basilisco y a las Sirenas:")
    for a_eliminar in ["Basilisco", "Sirenas"]:
        eliminado = arbol.eliminar(a_eliminar)
        if eliminado:
            print(f"-> Se eliminó a '{a_eliminar}' del árbol.")
    print()

    # k. Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias
    print("k. Modificar el nodo de 'Aves del Estínfalo' (Heracles derrotó a varias):")
    nodo_aves = arbol.buscar("Aves del Estínfalo")
    if nodo_aves:
        nodo_aves.derrotado_por = "Heracles (derrotó a varias)"
        print(f"-> 'Aves del Estínfalo' actualizado. Derrotado por: {nodo_aves.derrotado_por}")
    print()

    # l. Modifique el nombre de la criatura Ladón por Dragón Ladón
    print("l. Modificar el nombre de la criatura 'Ladón' por 'Dragón Ladón':")
    nodo_ladon = arbol.buscar("Ladón")
    if nodo_ladon:
        derrotado_val = nodo_ladon.derrotado_por
        capturada_val = nodo_ladon.capturada
        desc_val = nodo_ladon.descripcion
        arbol.eliminar("Ladón")
        arbol.insertar("Dragón Ladón", derrotado_por=derrotado_val, capturada=capturada_val, descripcion=desc_val)
        print("-> 'Ladón' fue eliminado y reinsertado como 'Dragón Ladón' para mantener el orden BST.")
    print()

    # d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
    print("d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
    conteo_derrotas = {}
    def _contar_derrotas(nodo):
        if nodo is not None:
            _contar_derrotas(nodo.izq)
            if nodo.derrotado_por and nodo.derrotado_por != "-":
                heroe = nodo.derrotado_por
                if "Heracles" in heroe:
                    heroe = "Heracles"
                conteo_derrotas[heroe] = conteo_derrotas.get(heroe, 0) + 1
            _contar_derrotas(nodo.der)

    _contar_derrotas(arbol.raiz)
    top_3 = sorted(conteo_derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
    for idx, (heroe, cant) in enumerate(top_3, 1):
        print(f" {idx}. {heroe}: {cant} criatura(s) derrotada(s)")
    print()

    # e. Listar las criaturas derrotadas por Heracles
    print("e. Listar las criaturas derrotadas por Heracles:")
    def _inorden_heracles(nodo):
        if nodo is not None:
            _inorden_heracles(nodo.izq)
            if nodo.derrotado_por and "Heracles" in nodo.derrotado_por:
                print(f"   - {nodo.nombre}")
            _inorden_heracles(nodo.der)
    _inorden_heracles(arbol.raiz)
    print()

    # f. Listar las criaturas que no han sido derrotadas
    print("f. Listar las criaturas que no han sido derrotadas:")
    def _inorden_no_derrotadas(nodo):
        if nodo is not None:
            _inorden_no_derrotadas(nodo.izq)
            if not nodo.derrotado_por or nodo.derrotado_por == "-":
                print(f"- {nodo.nombre}")
            _inorden_no_derrotadas(nodo.der)
    _inorden_no_derrotadas(arbol.raiz)
    print()

    # i. Búsquedas por coincidencia
    print("i. Búsqueda por coincidencia (ejemplo búsqueda de 'Dragón'):")
    coincidencias = arbol.busqueda_coincidencia("Dragón")
    for elem in coincidencias:
        print(f"- Encontrado: {elem.nombre} (Derrotado por: {elem.derrotado_por})")
    print()

    # m. Realizar un listado por nivel del árbol
    print("m. Listado por nivel del árbol:")
    arbol.barrido_por_nivel()
    print()

    # n. Muestre las criaturas capturadas por Heracles
    print("\nn. Criaturas capturadas por Heracles:")
    def _inorden_capturadas(nodo):
        if nodo is not None:
            _inorden_capturadas(nodo.izq)
            if nodo.capturada and "Heracles" in nodo.capturada:
                print(f"- {nodo.nombre}")
            _inorden_capturadas(nodo.der)
    _inorden_capturadas(arbol.raiz)
    print()


def main():
    ejecutar_ejercicio_23()


if __name__ == "__main__":
    main()
