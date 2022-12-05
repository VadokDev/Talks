CD = input("¿Qué quieres hacer, Codificar o Decodificar (C/D):? ")

#---CODIFICAR----
if CD == "C":
    texto0 = input("Texto a codificar: ")
    texto1 = ""
    # REEMPLAZAR LETRAS
    for caracter in texto0:
        if caracter == "a" or caracter == "á":
            texto1 += "e"
        elif caracter == "e" or caracter == "é":
            texto1 += "i"
        elif caracter == "i" or caracter == "í":
            texto1 += "o"
        elif caracter == "o" or caracter == "ó":
            texto1 += "u"
        elif caracter == "u" or caracter == "ú":
            texto1 += "a"
        elif caracter == "ñ":
            texto1 += "n"
        else:
            texto1 += caracter
    
    texto0 = ""
    i = 0
    j = 0
    
    # DAR VUELTA CADA PALABRA
    while i < len(texto1):
        palabra0 = ""
        palabra1 = ""

        #EXTRAER PALABRA
        while i < len(texto1) and texto1[i] != " ":
            i+= 1
        palabra0 = texto1[j:i]

        #DAR VUELTA PALABRA
        k = len(palabra0)
        while k > 0:
            palabra1 += palabra0[k-1]
            k -= 1
       
        k = 0

        #AGREGAR PALABRA INVERTIDA
        texto0 = texto0 + palabra1 + " "
        i += 1
        j = i

    print(texto0) 
    desplazamiento = int(input("Desplazamiento: "))
    
    # DESPLAZAR CADA LETRA
    texto1 = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    i=0
   
    for caracter in texto0:
        if caracter == " ":
            texto1 += caracter
        else:   
            for letra in alfabeto:
                if caracter == letra:
                    i += desplazamiento
                    
                    if i > len(alfabeto):
                        i = i % len(alfabeto)
                    elif i == 26:
                        i = 0
                    texto1 += alfabeto[i]
            
                else:
                    i +=1
        i=0


    print("Texto codificado:",texto1)
    
#----DECODIFICAR----
else:
    texto0 = input("Texto a decodificar: ")
    desplazamiento = int(input("Desplazamiento: "))

    # DESPLAZAR CADA LETRA
    texto1 = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    i=0
    
    for caracter in texto0:
        if caracter == " ":
            texto1 += caracter
        else:   
            for letra in alfabeto:
                if caracter == letra:
                    i -= desplazamiento
                    if i > len(alfabeto) or i < -len(alfabeto):
                        i = i % len(alfabeto)
                    elif i == 26:
                        i = 0
                    texto1 += alfabeto[i]
                else:
                    i +=1
        i=0
    
    texto0 = ""
    i = 0
    j = 0
    k = 0
    # DAR VUELTA CADA PALABRA
    while i < len(texto1):
        palabra0 = ""
        palabra1 = ""
        
        #EXTRAER PALABRA
        while i < len(texto1) and texto1[i] != " ":
            i+= 1
        palabra0 = texto1[j:i]

        #DAR VUELTA PALABRA
        k = len(palabra0)
        while k > 0:
            palabra1 += palabra0[k-1]
            k -= 1
      
        k = 0

        #AGREGAR PALABRA INVERTIDA
        texto0 = texto0 + palabra1 + " "
        i += 1
        j = i
    texto1 = ""

    # REEMPLAZAR LETRAS
    for caracter in texto0:
        if caracter == "e":
            texto1 += "a"
        elif caracter == "i":
            texto1 += "e"
        elif caracter == "o":
            texto1 += "i"
        elif caracter == "u":
            texto1 += "o"
        elif caracter == "a":
            texto1 += "u"
        else:
            texto1 += caracter
    print("Texto decodificado:",texto1)


        
