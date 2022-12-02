from direccion_de_estudios import *


def obtener_recinto(capacidad, lista_recinto, dia_bloque, asignados):
    lista = []
    for i in lista_recinto:
        if i[1] >= capacidad:  # Se filtran las salas por capacidad
            con = 0
            for j in asignados:  # Se filtran las salas por horario
                if i[0] == j[1]:
                    if j[2] == dia_bloque:
                        con += 1
            if con == 0:
                lista.append(i)
    for i in range(len(lista)-1):  # Se utiliza el ordenamiento burbuja para ordenar la lista de forma creciente
        for j in range(len(lista)-i-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    sala = []
    for j in lista:  # Se crea la lista que contiene las salas
        sala.append(j[0])
    return sala


for i in solicitudes:
    print("Procesando solicitud de", i[0]+"/"+str(i[1]), "...")
    if i[7] == "P":
        if i[6] == 1:  # Se determina la lista con la que se tratarán los datos en la función obtener_recinto()
            a = obtener_recinto(i[3], labs, i[5], asignados)
        else:
            a = obtener_recinto(i[3], salas, i[5], asignados)
        if len(a) == 0:  # Caso en el que la lista esté vacía (no hay salas disponibles)
            print(" No hay disponibilidad para", i[5])
            i[7] = "F"
        else:
            print(" ", a[0], "asignado para", i[5])
            nombre_par = i[0]+"/"+str(i[1])
            asignados.append([nombre_par, a[0], i[5], i[4]])
            i[7] = "R"
    else:
        print(" Procesada previamente")


"""  #  Si se requiere comprobar el estado de las listas...
print(asignados)
print(solicitudes)
"""
