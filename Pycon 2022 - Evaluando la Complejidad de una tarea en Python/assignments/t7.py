# {identificador: {"nombre": nombre_apellido, "ubicacion": [x,y]} }
identificador = {
    1 : {"nombre" : "Aitor Menta", "ubicacion" : [100, 3]},
    2 : {"nombre" : "Helen Chufe", "ubicacion" : [10, 23]},
    3 : {"nombre" : "Lola Mento", "ubicacion" : [45, 35]},
    4 : {"nombre" : "Zacarias Flores del Campo", "ubicacion" : [87, 34]}
}


# [ [id, edad, [hobbie1, hobbie2, ...], tipo_relación], ...]
personas =[
   [1, 21, ["programar", "cocinar", "videojuegos"], True],
   [2, 22, ["videojuegos", "mascotas"], False],
   [3, 23, ["cocinar", "tejer"], True],
   [4, 21, ["videojuegos", "mascotas", "tejer"], False]
]
def clasificar_hobbies(personas, amor):
    i=0
    lista={}
    lista2=[]
    anotados=[]
    while i<len(personas):
        while i<len(personas):
            persona=personas[i]
            if persona[3]==amor:
                t=0
                while t<len(persona[2]):
                    hobbies=persona[2]
                    if hobbies[t] not in lista:
                        lista[hobbies[t]]=[]
                        anotados.append(hobbies[t])
                    lista[hobbies[t]].append(1)
                    t+=1
            i+=1
    orden=[]
    i=0
    while i<len(anotados):
        orden.append(lista[anotados[i]])
        orden.sort(reverse=True)
        lugar=orden.index(lista[anotados[i]])
        new=[sum(lista[anotados[i]]),anotados[i]]
        lista2.insert(lugar,new)
        i+=1
    return lista2
def buscar(personas,identificador,hobbie,min,max):
    morax={}
    i=0
    while i<len(personas):
        persona=personas[i]
        if hobbie in persona[2] and min<=persona[1]<=max:
            if persona[1] not in morax:
                morax[persona[1]]=[]
            morgana=identificador[i+1]
            coordenadas=morgana["ubicacion"]
            pitagoro=round(((coordenadas[0]**2)+(coordenadas[1]**2))**(1/2),2)
            bollodecaca=[pitagoro, morgana["nombre"]]
            morax[persona[1]].append(bollodecaca)
            morax[persona[1]].sort()
        i+=1
    return morax
import time
busco={"amor":True , "jugar":False}
eleccion="PONME UN 1OO PORFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print("<Bienvenido a TIWINDER®>")
while eleccion!="3":
    print("¿Que deseas hacer?")
    print("(1) Consultar hobbie")
    print("(2) Buscar persona")
    print("(3) Salir")
    eleccion=input("Opción: ")
    while eleccion!="1" and eleccion!="2" and eleccion!="3":
        print("Por favor seleccione una opción valida")
        time.sleep(1)
        eleccion = input("Opción: ")
    print()
    if eleccion=="1":
        print("¿Que es lo que buscas? (amor/jugar)")
        fernanfloo=input().lower()
        while fernanfloo!="amor" and fernanfloo!="jugar":
            print("Por favor seleccione una opción valida")
            fernanfloo = input().lower()
        print("Por favor espere unos segundos...")
        amor=busco[fernanfloo]
        candidatos=clasificar_hobbies(personas, amor)
        i=0
        time.sleep(1)
        print()
        while i<len(candidatos):
            merus=candidatos[i]
            print(merus[0],"personas interesadas en",merus[1],"...")
            time.sleep(1)
            i+=1
        print("...que buscan",fernanfloo)
        time.sleep(2)
        print()
    if eleccion=="2":
        hobbie=input("Ingresa el hobby que te interesa: ")
        min=int(input("¿Cuál es la edad mínima?: "))
        if min<18:
            print("La edad mínima solicitada es inferior a lo admitido, su edad solcitada ha sido ajustada a 18")
            time.sleep(1)
            min=18
        if min>100:
            print("wow")
            time.sleep(1)
        max=int(input("¿Cuál es la edad máxima?: "))
        while max<min:
            print("La edad máxima debe ser menor o igual a la mínima")
            max = int(input("¿Cuál es la edad máxima?: "))
        print("Espere un momento...")
        candidatos=buscar(personas,identificador,hobbie,min,max)
        i=min
        encuentro=False
        while i<=max:
            if i in candidatos:
                encuentro=True
                print()
                lista=candidatos[i]
                t=0
                print("Hay",len(lista),"personas con",i,"años")
                time.sleep(1)
                while t<len(lista):
                    persona=lista[t]
                    print(persona[1],"está a",persona[0],"metros de distancia")
                    t+=1
            i+=1
        if encuentro==False:
            time.sleep(3)
            print("No encontramos personas con los parametros solicitados... :(")
        time.sleep(1)
        print()
print("¡Hasta Luego! Y recuerda, nunca es tarde para encontrar el amor")
time.sleep(3)