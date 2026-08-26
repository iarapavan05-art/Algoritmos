from super_heroes_data import superheroes

class NodoLista:
    def __init__(self, info): self.info, self.siguiente = info, None

class Lista:
    def __init__(self): self.inicio, self.tamanio = None, 0
    def insertar(self, elemento, campo=None):
        nuevo = NodoLista(elemento)
        valor = criterio(elemento, campo)
        if self.inicio is None or valor < criterio(self.inicio.info, campo):
            nuevo.siguiente = self.inicio; self.inicio = nuevo; self.tamanio += 1; return
        ant, act = self.inicio, self.inicio.siguiente
        while act is not None and criterio(act.info, campo) <= valor:
            ant, act = act, act.siguiente
        nuevo.siguiente = act; ant.siguiente = nuevo; self.tamanio += 1
    def eliminar(self, clave, campo=None):
        ant, act = None, self.inicio
        while act is not None:
            if criterio(act.info, campo) == clave:
                if ant is None: self.inicio = act.siguiente
                else: ant.siguiente = act.siguiente
                self.tamanio -= 1; return act.info
            ant, act = act, act.siguiente
        return None
    def buscar(self, clave, campo=None):
        act = self.inicio
        while act is not None:
            if criterio(act.info, campo) == clave: return act
            act = act.siguiente
        return None
    def lista_vacia(self): return self.inicio is None
    def tamaño(self): return self.tamanio
    def barrido(self):
        act = self.inicio
        while act is not None: print(act.info); act = act.siguiente

def criterio(dato, campo=None):
    if campo is None: return dato
    if isinstance(dato, dict): return dato.get(campo)
    return getattr(dato, campo, dato)

class NodoCola:
    def __init__(self, info): self.info, self.siguiente = info, None

class Cola:
    def __init__(self): self.frente, self.final, self.tamanio = None, None, 0
    def arribo(self, elemento):
        nuevo = NodoCola(elemento)
        if self.frente is None: self.frente = nuevo
        else: self.final.siguiente = nuevo
        self.final = nuevo; self.tamanio += 1
    def atencion(self):
        if self.frente is None: return None
        dato = self.frente.info; self.frente = self.frente.siguiente
        if self.frente is None: self.final = None
        self.tamanio -= 1; return dato
    def cola_vacia(self): return self.frente is None
    def en_frente(self): return None if self.frente is None else self.frente.info
    def tamaño(self): return self.tamanio
    def mover_al_final(self):
        if self.frente is None: return None
        dato = self.atencion(); self.arribo(dato); return dato

class NodoPila:
    def __init__(self, info): self.info, self.siguiente = info, None

class Pila:
    def __init__(self): self.cima, self.tamanio = None, 0
    def apilar(self, elemento):
        nuevo = NodoPila(elemento); nuevo.siguiente = self.cima; self.cima = nuevo; self.tamanio += 1
    def desapilar(self):
        if self.cima is None: return None
        dato = self.cima.info; self.cima = self.cima.siguiente; self.tamanio -= 1; return dato
    def pila_vacia(self): return self.cima is None
    def cima_elemento(self): return None if self.cima is None else self.cima.info
    def tamaño(self): return self.tamanio

def copiar_a_lista_ordenada(datos, campo):
    lista = Lista()
    for personaje in datos: lista.insertar(personaje, campo)
    return lista

# PUNTO 1
lista_superheroes = ["Iron Man", "Thor", "Hulk", "Capitan America", "Black Widow", "Hawkeye", "Spider-Man", "Doctor Strange", "Black Panther", "Wolverine", "Deadpool", "Flash", "Superman", "Batman", "Wonder Woman"]

def buscar_capitan(lista, indice=0):
    if indice == len(lista): return False
    if lista[indice] == "Capitan America": return True
    return buscar_capitan(lista, indice + 1)

def listar_superheroes(lista, indice=0):
    if indice == len(lista): return
    print(lista[indice]); listar_superheroes(lista, indice + 1)

print("==========================================")
print("PUNTO 1")
print("==========================================")
listar_superheroes(lista_superheroes)
print("Capitan America está en la lista." if buscar_capitan(lista_superheroes) else "Capitan America no está en la lista.")

# PUNTO 2
print("\n==========================================")
print("PUNTO 2")
print("==========================================")

lista_por_nombre = copiar_a_lista_ordenada(superheroes, "name")
print("\n1. Personajes ordenados por nombre:")
act = lista_por_nombre.inicio
while act is not None: print(act.info["name"]); act = act.siguiente

def buscar_posicion(lista, nombre):
    act, pos = lista.inicio, 0
    while act is not None:
        if act.info["name"] == nombre: return pos
        act, pos = act.siguiente, pos + 1
    return None

print("\n2. Posiciones:")
print("The Thing:", buscar_posicion(lista_por_nombre, "The Thing"))
print("Rocket Raccoon:", buscar_posicion(lista_por_nombre, "Rocket Raccoon"))

print("\n3. Villanos:")
for p in superheroes:
    if p["is_villain"]: print(p["name"])

cola_villanos = Cola()
for p in superheroes:
    if p["is_villain"]: cola_villanos.arribo(p)
print("\n4. Villanos que aparecieron antes de 1980:")
while not cola_villanos.cola_vacia():
    p = cola_villanos.atencion()
    if p["first_appearance"] < 1980: print(p["name"], "-", p["first_appearance"])

print("\n5. Superhéroes que comienzan con Bl, G, My y W:")
for p in superheroes:
    if p["name"].startswith(("Bl", "G", "My", "W")): print(p["name"])

orden_real = sorted(
    superheroes,
    key=lambda x: x["real_name"] or ""
)

print("\n6. Personajes ordenados por nombre real:")

for personaje in orden_real:

    print(
        personaje["real_name"],
        "-",
        personaje["name"]
    )


print("\n7. Superhéroes ordenados por fecha de aparición:")
orden_fecha = sorted(
    superheroes,
    key=lambda x: x["first_appearance"]
)


for personaje in orden_fecha:

    print(
        personaje["name"],
        "-",
        personaje["first_appearance"]
    )



for personaje in superheroes:

    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"


print("\n8. Ant Man modificado:")

for personaje in superheroes:

    if personaje["name"] == "Ant Man":
        print(
            personaje["name"],
            "-",
            personaje["real_name"]
        )



print("\n9. Personajes cuya biografía contiene")
print("'time-traveling' o 'suit':")

for personaje in superheroes:

    bio = personaje["short_bio"] or ""

    bio = bio.lower()

    if "time-traveling" in bio or "suit" in bio:

        print(
            personaje["name"],
            "-",
            personaje["short_bio"]
        )



eliminados = []

superheroes_filtrado = []

for personaje in superheroes:

    if personaje["name"] == "Electro" or personaje["name"] == "Baron Zemo":

        eliminados.append(personaje)

    else:

        superheroes_filtrado.append(personaje)


print("\n10. Personajes eliminados:")

if len(eliminados) > 0:

    for personaje in eliminados:

        print("\nNombre:", personaje["name"])
        print("Alias:", personaje["alias"])
        print("Nombre real:", personaje["real_name"])
        print("Biografía:", personaje["short_bio"])
        print("Primera aparición:", personaje["first_appearance"])
        print("¿Es villano?:", personaje["is_villain"])

else:

    print("No se encontró Electro ni Baron Zemo.")


# Actualizamos la lista
superheroes = superheroes_filtrado


print("\nLista actualizada correctamente.")
print("Cantidad de personajes restantes:", len(superheroes))