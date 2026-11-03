
import heapq
from collections import deque

# PUNTO A: crear el grafo y cargar los dispositivos
equipos = {
    "Manjaro": "pc",
    "Red Hat": "notebook",
    "Debian": "notebook",
    "Arch": "notebook",
    "Fedora": "pc",
    "Ubuntu": "pc",
    "Mint": "pc",
    "Switch 01": "switch",
    "Switch 02": "switch",
    "Router 01": "router",
    "Router 02": "router",
    "Guarani": "servidor",
    "MongoDB": "servidor",
    "Impresora": "impresora"
}

grafo = {equipo: [] for equipo in equipos}

def agregar_arista(a, b, peso):
    grafo[a].append((b, peso))
    grafo[b].append((a, peso))

# Conexiones de ejemplo: reemplazar por las de la figura
conexiones = [
    ("Manjaro", "Switch 01", 2),
    ("Red Hat", "Switch 01", 3),
    ("Debian", "Switch 01", 4),
    ("Arch", "Switch 02", 2),
    ("Fedora", "Switch 02", 3),
    ("Ubuntu", "Switch 01", 5),
    ("Mint", "Switch 02", 4),
    ("Switch 01", "Router 01", 2),
    ("Switch 02", "Router 01", 3),
    ("Switch 02", "Router 02", 2),
    ("Router 01", "Router 02", 4),
    ("Router 01", "Guarani", 3),
    ("Router 02", "MongoDB", 2),
    ("Router 01", "Impresora", 5),
    ("Router 02", "Impresora", 3),
    ("Switch 01", "Guarani", 8),
    ("Switch 02", "MongoDB", 6)
]

for a, b, peso in conexiones:
    agregar_arista(a, b, peso)

# Recorrido en profundidad
def profundidad(inicio):
    visitados = set()
    pila = [inicio]
    recorrido = []

    while pila:
        actual = pila.pop()
        if actual not in visitados:
            visitados.add(actual)
            recorrido.append(actual)
            for vecino, peso in reversed(grafo[actual]):
                if vecino not in visitados:
                    pila.append(vecino)
    return recorrido

# Recorrido en amplitud
def amplitud(inicio):
    visitados = {inicio}
    cola = deque([inicio])
    recorrido = []

    while cola:
        actual = cola.popleft()
        recorrido.append(actual)
        for vecino, peso in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return recorrido

# Camino más corto: algoritmo de Dijkstra
def dijkstra(origen, destino):
    distancias = {n: float("inf") for n in grafo}
    anteriores = {}
    distancias[origen] = 0
    cola = [(0, origen)]

    while cola:
        distancia, actual = heapq.heappop(cola)

        if distancia > distancias[actual]:
            continue
        if actual == destino:
            break

        for vecino, peso in grafo[actual]:
            nueva = distancia + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva, vecino))

    if distancias[destino] == float("inf"):
        return None, float("inf")

    camino = []
    actual = destino
    while actual != origen:
        camino.append(actual)
        actual = anteriores[actual]
    camino.append(origen)
    camino.reverse()

    return camino, distancias[destino]

# Árbol de expansión mínima: algoritmo de Prim
def prim(inicio):
    visitados = {inicio}
    disponibles = []
    arbol = []
    total = 0

    for vecino, peso in grafo[inicio]:
        heapq.heappush(disponibles, (peso, inicio, vecino))

    while disponibles and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(disponibles)

        if destino in visitados:
            continue

        visitados.add(destino)
        arbol.append((origen, destino, peso))
        total += peso

        for vecino, costo in grafo[destino]:
            if vecino not in visitados:
                heapq.heappush(
                    disponibles, (costo, destino, vecino)
                )

    return arbol, total

# MOSTRAR RESULTADOS DE TODA LA ACTIVIDAD
print("PUNTO A: DISPOSITIVOS DEL GRAFO")
for equipo, tipo in equipos.items():
    print(equipo, "-", tipo)

print("\nPUNTO B: RECORRIDOS EN PROFUNDIDAD Y AMPLITUD")
for inicio in ["Red Hat", "Debian", "Arch"]:
    print("\nDesde", inicio)
    print("Profundidad:", profundidad(inicio))
    print("Amplitud:", amplitud(inicio))

print("\nPUNTO C: CAMINO MAS CORTO HASTA LA IMPRESORA")
for inicio in ["Manjaro", "Red Hat", "Fedora"]:
    camino, distancia = dijkstra(inicio, "Impresora")
    print(inicio, ":", camino, "| Peso total:", distancia)

print("\nPUNTO D: ARBOL DE EXPANSION MINIMA")
arbol, total = prim("Manjaro")
for origen, destino, peso in arbol:
    print(origen, "--", destino, ":", peso)
print("Peso total:", total)

print("\nPUNTO E: PC CON CAMINO MAS CORTO A GUARANI")
pcs = [
    equipo for equipo, tipo in equipos.items()
    if tipo == "pc"
]
for pc in pcs:
    camino, distancia = dijkstra(pc, "Guarani")
    print(pc, ":", camino, "| Peso total:", distancia)

mejor_pc = min(
    pcs, key=lambda pc: dijkstra(pc, "Guarani")[1]
)
print("PC mas cercana a Guarani:", mejor_pc)

print("\nPUNTO F: COMPUTADORA DEL SWITCH 01 MAS CERCANA A MONGODB")
computadoras = [
    vecino for vecino, peso in grafo["Switch 01"]
    if equipos[vecino] in ("pc", "notebook")
]

for equipo in computadoras:
    camino, distancia = dijkstra(equipo, "MongoDB")
    print(equipo, ":", camino, "| Peso total:", distancia)

mejor = min(
    computadoras,
    key=lambda equipo: dijkstra(equipo, "MongoDB")[1]
)
print("Computadora mas cercana a MongoDB:", mejor)






#Ejercicio 14

import heapq

# Ambientes de la casa.
ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho",
    "Baño 1", "Baño 2", "Habitacion 1", "Habitacion 2",
    "Sala de estar", "Terraza", "Patio"
]

grafo = {ambiente: [] for ambiente in ambientes}

def agregar_arista(a, b, metros):
    grafo[a].append((b, metros))
    grafo[b].append((a, metros))

# Distancias de ejemplo expresadas en metros.
conexiones = [
    ("Cocina", "Comedor", 3),
    ("Cocina", "Baño 1", 4),
    ("Cocina", "Habitacion 1", 6),
    ("Cocina", "Sala de estar", 5),
    ("Cocina", "Patio", 8),

    ("Comedor", "Sala de estar", 2),
    ("Comedor", "Quincho", 7),
    ("Comedor", "Baño 2", 5),
    ("Comedor", "Terraza", 6),

    ("Cochera", "Quincho", 4),
    ("Cochera", "Patio", 3),
    ("Cochera", "Cocina", 9),

    ("Quincho", "Patio", 5),
    ("Quincho", "Terraza", 8),

    ("Baño 1", "Habitacion 1", 2),
    ("Baño 1", "Habitacion 2", 4),

    ("Baño 2", "Habitacion 2", 3),
    ("Baño 2", "Sala de estar", 6),

    ("Habitacion 1", "Habitacion 2", 3),
    ("Habitacion 1", "Sala de estar", 7),

    ("Habitacion 2", "Sala de estar", 2),
    ("Habitacion 2", "Terraza", 5),

    ("Sala de estar", "Terraza", 4),
    ("Sala de estar", "Patio", 7),

    ("Terraza", "Patio", 3)
]

for a, b, metros in conexiones:
    agregar_arista(a, b, metros)

# Dijkstra: encuentra el camino de menor distancia.
def dijkstra(origen, destino):
    distancias = {n: float("inf") for n in grafo}
    anteriores = {}
    distancias[origen] = 0
    cola = [(0, origen)]

    while cola:
        distancia, actual = heapq.heappop(cola)

        if distancia > distancias[actual]:
            continue

        if actual == destino:
            break

        for vecino, metros in grafo[actual]:
            nueva_distancia = distancia + metros

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(
                    cola, (nueva_distancia, vecino)
                )

    if distancias[destino] == float("inf"):
        return None, float("inf")

    camino = []
    actual = destino

    while actual != origen:
        camino.append(actual)
        actual = anteriores[actual]

    camino.append(origen)
    camino.reverse()

    return camino, distancias[destino]

# Prim: obtiene el árbol de expansión mínima.
def prim(inicio):
    visitados = {inicio}
    disponibles = []
    arbol = []
    total = 0

    for vecino, metros in grafo[inicio]:
        heapq.heappush(
            disponibles, (metros, inicio, vecino)
        )

    while disponibles and len(visitados) < len(grafo):
        metros, origen, destino = heapq.heappop(disponibles)

        if destino in visitados:
            continue

        visitados.add(destino)
        arbol.append((origen, destino, metros))
        total += metros

        for vecino, costo in grafo[destino]:
            if vecino not in visitados:
                heapq.heappush(
                    disponibles, (costo, destino, vecino)
                )

    return arbol, total

# Punto c: árbol de expansión mínima.
print("PUNTO C - ARBOL DE EXPANSION MINIMA")
arbol, total = prim("Cocina")

for origen, destino, metros in arbol:
    print(origen, "--", destino, ":", metros, "metros")

print("Cantidad total de cable:", total, "metros")

# Punto d: camino más corto entre Habitacion 1 y Sala de estar.
print("\nPUNTO D - CAMINO MAS CORTO")
camino, metros = dijkstra("Habitacion 1", "Sala de estar")

print("Camino:", " -> ".join(camino))
print("Cable de red necesario:", metros, "metros")
