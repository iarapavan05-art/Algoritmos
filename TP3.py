#ejercicio 10
from collections import deque

# Crear cola de notificaciones
def crear_cola_original():
    return deque([
        {"hora": "10:30", "app": "Facebook", "mensaje": "Nuevo comentario"},
        {"hora": "11:45", "app": "Twitter", "mensaje": "Aprendiendo Python"},
        {"hora": "12:10", "app": "Instagram", "mensaje": "Nueva foto"},
        {"hora": "13:20", "app": "Twitter", "mensaje": "Python es genial"},
        {"hora": "15:00", "app": "Facebook", "mensaje": "Nuevo like"},
        {"hora": "15:30", "app": "Twitter", "mensaje": "Hola mundo"},
    ])


# a) Eliminar notificaciones de Facebook

def eliminar_facebook(cola):
    nueva_cola = deque()
    
    while cola:
        notif = cola.popleft()
        if notif["app"] != "Facebook":
            nueva_cola.append(notif)
    
    return nueva_cola


# ---------------------------
# b) Mostrar notificaciones de Twitter con "Python" sin perder datos
# ---------------------------
def mostrar_twitter_python(cola):
    aux = deque()
    
    while cola:
        notif = cola.popleft()
        
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(notif)
        
        aux.append(notif)
    
    # restaurar cola original
    while aux:
        cola.append(aux.popleft())


# ---------------------------
# c) Usar pila para notificaciones entre 11:43 y 15:57
# ---------------------------
def contar_notificaciones_rango(cola):
    pila = []
    aux = deque()
    
    inicio = "11:43"
    fin = "15:57"
    
    while cola:
        notif = cola.popleft()
        
        if inicio <= notif["hora"] <= fin:
            pila.append(notif)
        
        aux.append(notif)
    
    # restaurar cola
    while aux:
        cola.append(aux.popleft())
    
    print("Cantidad en rango:", len(pila))
    return pila


# ---------------------------
# PRUEBAS INDEPENDIENTES
# ---------------------------

# Prueba a)
cola_a = crear_cola_original()
cola_a = eliminar_facebook(cola_a)
print("\na) Sin Facebook:")
for n in cola_a:
    print(n)

# Prueba b)
cola_b = crear_cola_original()
print("\nb) Twitter con Python:")
mostrar_twitter_python(cola_b)

# Prueba c)
cola_c = crear_cola_original()
print("\nc) Notificaciones en rango:")
pila = contar_notificaciones_rango(cola_c)




#ejercicio 22
from collections import deque

# Crear cola de personajes
cola = deque([
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Black Panther", "genero": "F"},
])


# ----------------------------------
# a) Nombre del personaje de Capitana Marvel
# ----------------------------------
def personaje_capitana_marvel(cola):
    aux = deque()
    resultado = None

    while cola:
        dato = cola.popleft()

        if dato["superheroe"] == "Capitana Marvel":
            resultado = dato["personaje"]

        aux.append(dato)

    cola.extend(aux)
    return resultado


# ----------------------------------
# b) Superhéroes femeninos
# ----------------------------------
def superheroes_femeninos(cola):
    aux = deque()

    print("Superhéroes femeninos:")
    while cola:
        dato = cola.popleft()

        if dato["genero"] == "F":
            print(dato["superheroe"])

        aux.append(dato)

    cola.extend(aux)


# ----------------------------------
# c) Personajes masculinos
# ----------------------------------
def personajes_masculinos(cola):
    aux = deque()

    print("Personajes masculinos:")
    while cola:
        dato = cola.popleft()

        if dato["genero"] == "M":
            print(dato["personaje"])

        aux.append(dato)

    cola.extend(aux)


# ----------------------------------
# d) Superhéroe de Scott Lang
# ----------------------------------
def superheroe_scott_lang(cola):
    aux = deque()
    resultado = None

    while cola:
        dato = cola.popleft()

        if dato["personaje"] == "Scott Lang":
            resultado = dato["superheroe"]

        aux.append(dato)

    cola.extend(aux)
    return resultado


# ----------------------------------
# e) Datos cuyos nombres comienzan con S
# ----------------------------------
def nombres_con_s(cola):
    aux = deque()

    print("Personajes o superhéroes que empiezan con S:")
    while cola:
        dato = cola.popleft()

        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print(dato)

        aux.append(dato)

    cola.extend(aux)


# ----------------------------------
# f) Buscar Carol Danvers
# ----------------------------------
def buscar_carol(cola):
    aux = deque()
    encontrado = False

    while cola:
        dato = cola.popleft()

        if dato["personaje"] == "Carol Danvers":
            print("Está en la cola. Su superhéroe es:", dato["superheroe"])
            encontrado = True

        aux.append(dato)

    cola.extend(aux)

    if not encontrado:
        print("No se encontró a Carol Danvers")


# ----------------------------------
# PRUEBAS
# ----------------------------------

print("a) Personaje de Capitana Marvel:", personaje_capitana_marvel(cola))

print("\nb)")
superheroes_femeninos(cola)

print("\nc)")
personajes_masculinos(cola)

print("\nd) Superhéroe de Scott Lang:", superheroe_scott_lang(cola))

print("\ne)")
nombres_con_s(cola)

print("\nf)")
buscar_carol(cola)
