from list_ import List
from super_heroes_data import superheroes 

# punto uno 
superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Capitan America",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Wolverine",
    "Deadpool",
    "Flash",
    "Superman",
    "Batman",
    "Wonder Woman"
]


def buscar_capitan(lista, indice=0):
    
    if indice == len(lista):
        return False


    if lista[indice] == "Capitan America":
        return True

    
    return buscar_capitan(lista, indice + 1)


def listar_superheroes(lista, indice=0):

    if indice == len(lista):
        return

    
    print(lista[indice])


    listar_superheroes(lista, indice + 1)


# Programa principal
print("Lista de superhéroes:")
listar_superheroes(superheroes)

print("\nBúsqueda de Capitan America:")
if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")



#punto dos

from collections import deque
from super_heroes_data import superheroes 

orden_nombre = sorted(superheroes, key=lambda x: x["name"])
print("Ordenados por nombre:")
for p in orden_nombre:
    print(p["name"])


def buscar_posicion(nombre):
    for i, p in enumerate(superheroes):
        if p["name"] == nombre:
            return i
    return None

print("\nPosiciones:")
print("The Thing:", buscar_posicion("The Thing"))
print("Rocket Raccoon:", buscar_posicion("Rocket Raccoon"))

 
villanos = [p for p in superheroes if p["is_villain"]]
print("\nVillanos:")
for v in villanos:
    print(v["name"])

 
cola_villanos = deque(villanos)

print("\nVillanos antes de 1980:")
for v in cola_villanos:
    if v["first_appearance"] < 1980:
        print(v["name"], "-", v["first_appearance"])

 
print("\nSuperhéroes con prefijos específicos:")
for p in superheroes:
    if p["name"].startswith(("Bl", "G", "My", "W")):
        print(p["name"])

 
orden_real = sorted(superheroes, key=lambda x: x["real_name"] or "")

print("\nOrdenados por nombre real:")
for p in orden_real:
    print(p["real_name"], "-", p["name"])

 
orden_fecha = sorted(superheroes, key=lambda x: int(x["first_appearance"]))

print("\nOrdenados por fecha:")
for p in orden_fecha:
    print(p["name"], "-", p["first_appearance"])

 
for p in superheroes:
    if p["name"] == "Ant Man":
        p["real_name"] = "Scott Lang"

print("\nAnt Man modificado correctamente")

 
print("\nCon 'time-traveling' o 'suit':")
for p in superheroes:
    bio = (p["short_bio"] or "").lower()
    if "time-traveling" in bio or "suit" in bio:
        print(p["name"])

 
eliminados = []

superheroes_filtrado = []

for p in superheroes:
    if p["name"] in ["Electro", "Baron Zemo"]:
        eliminados.append(p)
    else:
        superheroes_filtrado.append(p)

print("\nEliminados:")
for e in eliminados:
    print(e)

# actualizar lista
superheroes = superheroes_filtrado