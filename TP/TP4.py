#Ejercicio 6

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
            print(f"{nombre}")
    else:
        print("Ninguno encontrado.")


def punto_e_anteriores_1963(lista):
    print("e. Superhéroes con fecha de aparición anterior a 1963:")
    anteriores = []
    for hero in lista:
        if hero.anio_aparicion < 1963:
            anteriores.append((hero.nombre, hero.casa, hero.anio_aparicion))

    if anteriores:
        for nombre, casa, anio in anteriores:
            print(f"Nombre: {nombre} | Casa: {casa} (Año: {anio})")
    else:
        print("Ninguno anterior a 1963.")


def punto_f_casa_capitana_marvel_y_mujer_maravilla(lista):
    print("f. Casa a la que pertenecen Capitana Marvel y Mujer Maravilla:")
    objetivos = ["capitana marvel", "mujer maravilla"]
    for hero in lista:
        if hero.nombre.lower() in objetivos:
            print(f"{hero.nombre} pertenece a: {hero.casa}")


def punto_g_informacion_flash_y_starlord(lista):
    print("g. Información completa de Flash y Star-Lord:")
    objetivos = ["flash", "star-lord", "starlord"]
    for hero in lista:
        if hero.nombre.lower() in objetivos:
            print(f"{hero}")


def punto_h_listar_iniciales_b_m_s(lista):
    print("h. Superhéroes que comienzan con las letras B, M y S:")
    iniciales = ('B', 'M', 'S')
    coincidencias = []
    for hero in lista:
        if hero.nombre.upper().startswith(iniciales):
            coincidencias.append(hero.nombre)

    if coincidencias:
        for nombre in coincidencias:
            print(f"{nombre}")
    else:
        print("Ninguno encontrado.")


def punto_i_contar_por_casa(lista):
    print("i. Cantidad de superhéroes por casa de cómic:")
    conteo = {}
    for hero in lista:
        casa = hero.casa
        conteo[casa] = conteo.get(casa, 0) + 1

    for casa, cantidad in conteo.items():
        print(f"{casa}: {cantidad} superhéroe(s)")


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








#Ejercicio 15

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo="Ninguno"):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        sub = f" / {self.subtipo}" if self.subtipo and self.subtipo.lower() != "ninguno" else ""
        return f"{self.nombre} (Nivel {self.nivel}, Tipo: {self.tipo}{sub})"


class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = [] 

    @property
    def batallas_totales(self):
        return self.batallas_ganadas + self.batallas_perdidas

    @property
    def porcentaje_victorias(self):
        if self.batallas_totales == 0:
            return 0.0
        return (self.batallas_ganadas / self.batallas_totales) * 100

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def __str__(self):
        return (f"Entrenador: {self.nombre} | Torneos Ganados: {self.torneos_ganados} | "
                f"Batallas: {self.batallas_ganadas}G / {self.batallas_perdidas}P "
                f"({self.porcentaje_victorias:.2f}% victorias)")



# a. Obtener la cantidad de Pokémons de un determinado entrenador
def obtener_cantidad_pokemons(lista_entrenadores, nombre_entrenador):
    for entrenador in lista_entrenadores:
        if entrenador.nombre.lower() == nombre_entrenador.lower():
            return len(entrenador.pokemons)
    return None


# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos(lista_entrenadores):
    return [e for e in lista_entrenadores if e.torneos_ganados > 3]


# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_del_mejor_entrenador(lista_entrenadores):
    if not lista_entrenadores:
        return None, None

    # Encontrar entrenador con mayor cantidad de torneos ganados
    mejor_entrenador = max(lista_entrenadores, key=lambda e: e.torneos_ganados)

    if not mejor_entrenador.pokemons:
        return mejor_entrenador, None

    # Encontrar el Pokémon de mayor nivel de ese entrenador
    pokemon_max = max(mejor_entrenador.pokemons, key=lambda p: p.nivel)
    return mejor_entrenador, pokemon_max


# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(lista_entrenadores, nombre_entrenador):
    for entrenador in lista_entrenadores:
        if entrenador.nombre.lower() == nombre_entrenador.lower():
            print(entrenador)
            print("Pokémons:")
            if entrenador.pokemons:
                for poke in entrenador.pokemons:
                    print(f"{poke}")
            else:
                print("(No tiene Pokémons registrados)")
            return True
    return False


# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def entrenadores_porcentaje_mayor_79(lista_entrenadores):
    return [e for e in lista_entrenadores if e.porcentaje_victorias > 79.0]


# f. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_con_tipos_especificos(lista_entrenadores):
    resultado = []
    for e in lista_entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False

        # Caso 1: El Pokémon mismo es Fuego/Planta o Agua/Volador (en tipo y subtipo)
        # Caso 2: El entrenador posee Pokémons de tipo Fuego y también Pokémons de tipo Planta
        tiene_fuego = False
        tiene_planta = False

        for p in e.pokemons:
            t = p.tipo.lower()
            st = p.subtipo.lower()

            # Verificación del tipo y subtipo del Pokémon
            if (t == "fuego" and st == "planta") or (t == "planta" and st == "fuego"):
                tiene_fuego_planta = True
            if (t == "agua" and st == "volador") or (t == "volador" and st == "agua"):
                tiene_agua_volador = True

            if t == "fuego" or st == "fuego":
                tiene_fuego = True
            if t == "planta" or st == "planta":
                tiene_planta = True

        if (tiene_fuego and tiene_planta) or tiene_fuego_planta or tiene_agua_volador:
            resultado.append(e)

    return resultado


# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons_entrenador(lista_entrenadores, nombre_entrenador):
    for e in lista_entrenadores:
        if e.nombre.lower() == nombre_entrenador.lower():
            if not e.pokemons:
                return 0.0
            total_niveles = sum(p.nivel for p in e.pokemons)
            return total_niveles / len(e.pokemons)
    return None


# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def contar_entrenadores_con_pokemon(lista_entrenadores, nombre_pokemon):
    contador = 0
    for e in lista_entrenadores:
        if any(p.nombre.lower() == nombre_pokemon.lower() for p in e.pokemons):
            contador += 1
    return contador


# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(lista_entrenadores):
    resultado = []
    for e in lista_entrenadores:
        nombres_pokemons = [p.nombre.lower() for p in e.pokemons]
        # Si la cantidad total es distinta a la cantidad de nombres únicos, hay repetidos
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(e)
    return resultado


# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos(lista_entrenadores):
    objetivos = {"tyrantrum", "terrakion", "wingull"}
    resultado = []
    for e in lista_entrenadores:
        nombres_pokes = {p.nombre.lower() for p in e.pokemons}
        if nombres_pokes.intersection(objetivos):
            resultado.append(e)
    return resultado


# k. Determinar si un entrenador "X" tiene al Pokémon "Y", ingresados por parámetro o teclado
def buscar_entrenador_y_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    for e in lista_entrenadores:
        if e.nombre.lower() == nombre_entrenador.lower():
            poke_encontrado = next((p for p in e.pokemons if p.nombre.lower() == nombre_pokemon.lower()), None)
            if poke_encontrado:
                return e, poke_encontrado
            return e, None
    return None, None


def cargar_datos_ejemplo():
    # Entrenador 1: Ash Ketchum
    ash = Entrenador("Ash Ketchum", torneos_ganados=5, batallas_perdidas=10, batallas_ganadas=90)
    ash.agregar_pokemon(Pokemon("Pikachu", 85, "Eléctrico"))
    ash.agregar_pokemon(Pokemon("Charizard", 78, "Fuego", "Volador"))
    ash.agregar_pokemon(Pokemon("Bulbasaur", 50, "Planta", "Veneno"))
    ash.agregar_pokemon(Pokemon("Tyrantrum", 65, "Roca", "Dragón"))
    ash.agregar_pokemon(Pokemon("Pikachu", 30, "Eléctrico"))  # Pokémon repetido

    # Entrenador 2: Misty
    misty = Entrenador("Misty", torneos_ganados=2, batallas_perdidas=5, batallas_ganadas=20)
    misty.agregar_pokemon(Pokemon("Gyarados", 70, "Agua", "Volador"))
    misty.agregar_pokemon(Pokemon("Psyduck", 40, "Agua"))
    misty.agregar_pokemon(Pokemon("Starmie", 55, "Agua", "Psíquico"))

    # Entrenador 3: Brock
    brock = Entrenador("Brock", torneos_ganados=4, batallas_perdidas=15, batallas_ganadas=35)
    brock.agregar_pokemon(Pokemon("Onix", 62, "Roca", "Tierra"))
    brock.agregar_pokemon(Pokemon("Geodude", 45, "Roca", "Tierra"))
    brock.agregar_pokemon(Pokemon("Scovillain", 52, "Fuego", "Planta"))
    brock.agregar_pokemon(Pokemon("Terrakion", 75, "Roca", "Lucha"))

    # Entrenador 4: Cynthia
    cynthia = Entrenador("Cynthia", torneos_ganados=8, batallas_perdidas=2, batallas_ganadas=98)
    cynthia.agregar_pokemon(Pokemon("Garchomp", 88, "Dragón", "Tierra"))
    cynthia.agregar_pokemon(Pokemon("Lucario", 75, "Lucha", "Acero"))
    cynthia.agregar_pokemon(Pokemon("Togekiss", 72, "Hada", "Volador"))
    cynthia.agregar_pokemon(Pokemon("Milotic", 74, "Agua"))

    # Entrenador 5: Roy
    roy = Entrenador("Roy", torneos_ganados=1, batallas_perdidas=20, batallas_ganadas=10)
    roy.agregar_pokemon(Pokemon("Wingull", 25, "Agua", "Volador"))
    roy.agregar_pokemon(Pokemon("Wingull", 12, "Agua", "Volador"))  # Pokémon repetido

    lista_entrenadores = [ash, misty, brock, cynthia, roy]
    return lista_entrenadores


def main():
    lista_entrenadores = cargar_datos_ejemplo()


    # a. Cantidad de Pokémons de un entrenador
    print("a- Cantidad de Pokémons de un determinado entrenador")
    entrenador_a = "Ash Ketchum"
    cant = obtener_cantidad_pokemons(lista_entrenadores, entrenador_a)
    if cant is not None:
        print(f"El entrenador '{entrenador_a}' tiene {cant} Pokémons.\n")
    else:
        print(f"El entrenador '{entrenador_a}' no fue encontrado.\n")

    # b. Entrenadores con más de 3 torneos ganados
    print("b- Entrenadores que hayan ganado más de 3 torneos")
    mas_3 = entrenadores_mas_de_tres_torneos(lista_entrenadores)
    for e in mas_3:
        print(f"{e.nombre} ({e.torneos_ganados} torneos ganados)")
    print()

    # c. Pokémon de mayor nivel del entrenador con más torneos ganados
    print("c- Pokémon de mayor nivel del entrenador con más torneos ganados")
    mejor_ent, poke_max = pokemon_mayor_nivel_del_mejor_entrenador(lista_entrenadores)
    if mejor_ent and poke_max:
        print(f"Entrenador con más torneos: {mejor_ent.nombre} ({mejor_ent.torneos_ganados} torneos)")
        print(f"Su Pokémon de mayor nivel es: {poke_max}\n")

    # d. Mostrar todos los datos de un entrenador y sus Pokémons
    print("d- Mostrar todos los datos de un entrenador y sus Pokémons")
    mostrar_datos_entrenador(lista_entrenadores, "Misty")
    print()

    # e. Entrenadores con porcentaje de batallas ganadas > 79%
    print("e- Entrenadores con victorias > 79%")
    mas_79 = entrenadores_porcentaje_mayor_79(lista_entrenadores)
    for e in mas_79:
        print(f"{e.nombre}: {e.porcentaje_victorias:.2f}% de victorias ({e.batallas_ganadas}G / {e.batallas_totales} totales)")
    print()

    # f. Entrenadores con Pokémons tipo fuego y planta o agua/volador
    print("f- Entrenadores con Pokémons de tipo Fuego/Planta o Agua/Volador")
    especificos = entrenadores_con_tipos_especificos(lista_entrenadores)
    for e in especificos:
        print(f"{e.nombre}")
    print()

    # g. Promedio de nivel de Pokémons de un entrenador
    print("g- Promedio de nivel de Pokémons de un determinado entrenador")
    entrenador_g = "Cynthia"
    prom = promedio_nivel_pokemons_entrenador(lista_entrenadores, entrenador_g)
    if prom is not None:
        print(f"El promedio de nivel de los Pokémons de '{entrenador_g}' es: {prom:.2f}\n")

    # h. Cuántos entrenadores tienen a un determinado Pokémon
    print("h- Cantidad de entrenadores que tienen a un determinado Pokémon")
    poke_h = "Pikachu"
    cant_ent = contar_entrenadores_con_pokemon(lista_entrenadores, poke_h)
    print(f"{cant_ent} entrenador(es) tienen a '{poke_h}'.\n")

    # i. Entrenadores que tienen Pokémons repetidos
    print("i- Entrenadores que tienen Pokémons repetidos")
    repetidos = entrenadores_con_pokemons_repetidos(lista_entrenadores)
    for e in repetidos:
        print(f" {e.nombre}")
    print()

    # j. Entrenadores que tienen a Tyrantrum, Terrakion o Wingull
    print("j- Entrenadores con Tyrantrum, Terrakion o Wingull")
    con_especiales = entrenadores_con_pokemons_especificos(lista_entrenadores)
    for e in con_especiales:
        pokes_nombres = [p.nombre for p in e.pokemons if p.nombre.lower() in {"tyrantrum", "terrakion", "wingull"}]
        print(f"  - {e.nombre} tiene: {', '.join(pokes_nombres)}")
    print()

    # k. Determinar si un entrenador X tiene al Pokémon Y
    print("k- Verificar si entrenador 'X' tiene al Pokémon 'Y'")
    nombre_x = "Ash Ketchum"
    nombre_y = "Tyrantrum"
    ent, poke = buscar_entrenador_y_pokemon(lista_entrenadores, nombre_x, nombre_y)

    if ent is None:
        print(f"El entrenador '{nombre_x}' no fue encontrado.")
    elif poke is None:
        print(f"El entrenador '{nombre_x}' NO tiene al Pokémon '{nombre_y}'.")
    else:
        print(f"¡Encontrado! El entrenador '{nombre_x}' SI tiene a '{nombre_y}'.")
        print("Datos del Entrenador:")
        print(f"{ent}")
        print("Datos del Pokémon:")
        print(f"{poke}")


if __name__ == "__main__":
    main()
