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


# b) Mostrar notificaciones de Twitter con "Python" sin perder datos

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



# c) Usar pila para notificaciones entre 11:43 y 15:57

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

# PRUEBAS INDEPENDIENTES


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



# a) Nombre del personaje de Capitana Marvel

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


#
# b) Superhéroes femeninos

def superheroes_femeninos(cola):
    aux = deque()

    print("Superhéroes femeninos:")
    while cola:
        dato = cola.popleft()

        if dato["genero"] == "F":
            print(dato["superheroe"])

        aux.append(dato)

    cola.extend(aux)


# c) Personajes masculinos

def personajes_masculinos(cola):
    aux = deque()

    print("Personajes masculinos:")
    while cola:
        dato = cola.popleft()

        if dato["genero"] == "M":
            print(dato["personaje"])

        aux.append(dato)

    cola.extend(aux)

# d) Superhéroe de Scott Lang

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

# e) Datos cuyos nombres comienzan con S

def nombres_con_s(cola):
    aux = deque()

    print("Personajes o superhéroes que empiezan con S:")
    while cola:
        dato = cola.popleft()

        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print(dato)

        aux.append(dato)

    cola.extend(aux)

# f) Buscar Carol Danvers

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


# PRUEBAS


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






# TP4 - Ejercicio 6: Lista de Superhéroes

class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return f"Nombre: {self.nombre} | Año: {self.anio_aparicion} | Casa: {self.casa} | Biografía: {self.biografia}"


class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def insertar(self, info):
        nuevo_nodo = Nodo(info)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.sig is not None:
                actual = actual.sig
            actual.sig = nuevo_nodo
        self.tamanio += 1

    def eliminar(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.info.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.sig
                else:
                    anterior.sig = actual.sig
                self.tamanio -= 1
                return actual.info
            anterior = actual
            actual = actual.sig
        return None

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.info
            actual = actual.sig



def punto_a_eliminar_linterna_verde(lista):
    eliminado = lista.eliminar("Linterna Verde")
    if eliminado:
        print(f"a. Se eliminó a '{eliminado.nombre}' de la lista con éxito.")
    else:
        print("a. Linterna Verde no se encontró en la lista.")


def punto_b_mostrar_anio_wolverine(lista):
    print("b. Año de aparición de Wolverine:")
    encontrado = False
    for hero in lista:
        if hero.nombre.lower() == "wolverine":
            print(f"   -> Wolverine apareció en el año: {hero.anio_aparicion}")
            encontrado = True
            break
    if not encontrado:
        print("   -> Wolverine no se encuentra en la lista.")


def punto_c_cambiar_casa_dr_strange(lista):
    print("c. Cambiar casa de Dr. Strange a Marvel:")
    encontrado = False
    for hero in lista:
        if "dr" in hero.nombre.lower() and "strange" in hero.nombre.lower():
            casa_anterior = hero.casa
            hero.casa = "Marvel"
            print(f"   -> {hero.nombre}: casa cambiada de '{casa_anterior}' a '{hero.casa}'.")
            encontrado = True
            break
    if not encontrado:
        print("   -> Dr. Strange no se encuentra en la lista.")


def punto_d_buscar_traje_o_armadura(lista):
    print("d. Superhéroes que mencionan 'traje' o 'armadura' en su biografía:")
    coincidencias = []
    for hero in lista:
        bio_lower = hero.biografia.lower()
        if "traje" in bio_lower or "armadura" in bio_lower:
            coincidencias.append(hero.nombre)

    if coincidencias:
        for nombre in coincidencias:
            print(f"   - {nombre}")
    else:
        print("   - Ninguno encontrado.")


def punto_e_anteriores_1963(lista):
    print("e. Superhéroes con fecha de aparición anterior a 1963:")
    anteriores = []
    for hero in lista:
        if hero.anio_aparicion < 1963:
            anteriores.append((hero.nombre, hero.casa, hero.anio_aparicion))

    if anteriores:
        for nombre, casa, anio in anteriores:
            print(f"   - Nombre: {nombre} | Casa: {casa} (Año: {anio})")
    else:
        print("   - Ninguno anterior a 1963.")


def punto_f_casa_capitana_marvel_y_mujer_maravilla(lista):
    print("f. Casa a la que pertenecen Capitana Marvel y Mujer Maravilla:")
    objetivos = ["capitana marvel", "mujer maravilla"]
    for hero in lista:
        if hero.nombre.lower() in objetivos:
            print(f"   - {hero.nombre} pertenece a: {hero.casa}")


def punto_g_informacion_flash_y_starlord(lista):
    print("g. Información completa de Flash y Star-Lord:")
    objetivos = ["flash", "star-lord", "starlord"]
    for hero in lista:
        if hero.nombre.lower() in objetivos:
            print(f"   - {hero}")


def punto_h_listar_iniciales_b_m_s(lista):
    print("h. Superhéroes que comienzan con las letras B, M y S:")
    iniciales = ('B', 'M', 'S')
    coincidencias = []
    for hero in lista:
        if hero.nombre.upper().startswith(iniciales):
            coincidencias.append(hero.nombre)

    if coincidencias:
        for nombre in coincidencias:
            print(f"   - {nombre}")
    else:
        print("   - Ninguno encontrado.")


def punto_i_contar_por_casa(lista):
    print("i. Cantidad de superhéroes por casa de cómic:")
    conteo = {}
    for hero in lista:
        casa = hero.casa
        conteo[casa] = conteo.get(casa, 0) + 1

    for casa, cantidad in conteo.items():
        print(f"   - {casa}: {cantidad} superhéroe(s)")


def main():
    # Creación de la lista enlazada
    lista_heroes = ListaEnlazada()

    # Datos iniciales de superhéroes
    datos_heroes = [
        Superheroe("Linterna Verde", 1940, "DC", "Miembro de los Green Lantern Corps. Utiliza un traje y un anillo de poder."),
        Superheroe("Wolverine", 1974, "Marvel", "Mutante poseedor de garras de adamantium y factor curativo."),
        Superheroe("Dr. Strange", 1963, "DC", "Sorcerer Supreme de la Tierra. Viste una capa mágica."), # Puesto en DC inicialmente para demostrar el cambio a Marvel
        Superheroe("Flash", 1940, "DC", "Conocido como el velocista escarlata, viste un traje especial para la súper velocidad."),
        Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, equipado con una armadura espacial y armas de alta tecnología."),
        Superheroe("Capitana Marvel", 1967, "Marvel", "Guerrera con poderes cósmicos gigantescos y fuerza sobrehumana."),
        Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con fuerza sobrehumana, usa un traje distintivo y el lazo de la verdad."),
        Superheroe("Batman", 1939, "DC", "El Caballero de la Noche de Ciudad Gótica. Utiliza un traje táctico avanza y gran tecnología."),
        Superheroe("Superman", 1938, "DC", "El Hombre de Acero proveniente del planeta Krypton."),
        Superheroe("Spider-Man", 1962, "Marvel", "Joven héroe con habilidades arácnidas que viste un traje rojo y azul."),
        Superheroe("Iron Man", 1963, "Marvel", "Empresario e inventor millonario que viste una armadura de alta tecnología."),
        Superheroe("Magneto", 1963, "Marvel", "Mutante con la capacidad de controlar campos magnéticos, viste un casco y armadura leve.")
    ]

    for hero in datos_heroes:
        lista_heroes.insertar(hero)    

    punto_a_eliminar_linterna_verde(lista_heroes)
    print()
    punto_b_mostrar_anio_wolverine(lista_heroes)
    print()
    punto_c_cambiar_casa_dr_strange(lista_heroes)
    print()
    punto_d_buscar_traje_o_armadura(lista_heroes)
    print()
    punto_e_anteriores_1963(lista_heroes)
    print()
    punto_f_casa_capitana_marvel_y_mujer_maravilla(lista_heroes)
    print()
    punto_g_informacion_flash_y_starlord(lista_heroes)
    print()
    punto_h_listar_iniciales_b_m_s(lista_heroes)
    print()
    punto_i_contar_por_casa(lista_heroes)
    print()

if __name__ == "__main__":
    main()