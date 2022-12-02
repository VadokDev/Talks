from funciones21 import *

# Valor (suma) de la mano del jugador
def obtener_valor(mano):
    j = 0
    i = 0
    total = 0
    while i < len(mano):
        if mano[i] == "♥" or mano[i] == "♦" or mano[i] == "♠" or mano[i] == "♣":
            numero = mano[j:i]
            if numero == "J" or numero == "Q" or numero == "K":
                numero = 10
            elif numero == "A":
                hay_A = True
                numero = 11
            else:
                numero = int(numero)
            total += numero
            if total > 21 and hay_A == True:
                total -= 10
            j = i + 2
            hay_A = False
        i += 1
    return total

#función leer la primera carta
def leer_primera_carta(mazo):
    i = 0
    while i < len(mazo):
        if mazo[i] == "-":
            primera_carta = mazo[:i]
            return primera_carta
        i += 1

#BLAKJAK
mazo = generar_mazo()

nombre = input("¿Como te llamas? ")
#Darme dos cartas
primera = leer_primera_carta(mazo)
mazo = eliminar_primera_carta(mazo)
segunda = leer_primera_carta(mazo)
mazo = eliminar_primera_carta(mazo)
mano = primera + "-" +segunda
print("Mano inicial " + nombre + ": " + mano)

#Dar una carta a Kiwi
manoK = leer_primera_carta(mazo)
print("Mano inicial Kiwi:", manoK)
mazo = eliminar_primera_carta(mazo)


# PRIMERA ETAPA
print("Turno " + nombre)
print("Tus cartas: " + mano)
print("Valor mano: ", obtener_valor(mano))

flag = True
suma = obtener_valor(mano)

while suma <= 21 and flag == True:

    print("¿Que desea hacer?")
    print("(1) Pedir carta")
    print("(2) Pasar")
    elección = int(input())

    if elección == 1:
        carta = leer_primera_carta(mazo)
        mazo = eliminar_primera_carta(mazo)
        mano = mano + "-" + carta
        print("Tus cartas:", mano)
        suma = obtener_valor(mano)
        print("Valor mano:", suma)

    else:
        print("Tus cartas:",mano)
        suma = obtener_valor(mano)
        print("Valor mano:", suma)
        flag = False

if suma > 21:
    print(nombre,"pierde. Gana Kiwi.")
else:
    # SEGUNDA ETAPA
    print("Turno Kiwi")
    print("Cartas de Kiwi:",manoK)
    valorK = obtener_valor(manoK)
    while valorK < suma:
        print("Kiwi saco una carta")
        carta = leer_primera_carta(mazo)
        mazo = eliminar_primera_carta(mazo)
        manoK = manoK + "-" + carta
        print("Cartas de Kiwi",manoK)
        valorK = obtener_valor(manoK)
        print("Valor mano:", valorK)

    if valorK == suma:
        print(Empate)
    elif valorK > 21:
        print("Kiwi pierde. Gana " + nombre)
    else:
        print(nombre +" pierde. Gana Kiwi.")

