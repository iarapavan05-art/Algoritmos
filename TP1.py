# Ejercicio 5

def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romano = romano.upper()     #Agrego para las minusculas.
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])

print(romano_a_decimal("III"))
print(romano_a_decimal("XXIII"))        #Mayuscula
print(romano_a_decimal("xxiii"))        #Minuscula
print(romano_a_decimal("MMCCCLXVIII"))

# Ejercicio 22
def usar_la_fuerza(mochila, indice=0, contador=0):

    if indice >= len(mochila):
        print("No se encontró un sable de luz")
        print("Se revisaron", contador, "objetos")
        return 
    print("Sacando:", mochila[indice])

    if mochila[indice].lower() == "sable de luz":
        print("Se encontró un sable de luz")
        print("Objetos revisados:", contador + 1)
        return 
    usar_la_fuerza(mochila, indice + 1, contador + 1)


mochila = ["cuaderno", "botella", "cartuchera", "sable de luz", "notebook"]

usar_la_fuerza(mochila)