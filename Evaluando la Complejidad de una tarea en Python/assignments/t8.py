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
