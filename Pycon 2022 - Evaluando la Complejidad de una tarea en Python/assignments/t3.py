
producto=input("Producto a analizar: ")

corte = True
precio_mayor= -1
precio_menor=9999999
precio_suma=0
nombre_menor=" "
nombre_mayor=" "
cant_fondas=0
while corte:

    fonda=input("Ingrese nombre de la fonda: ")
    if fonda!="FIN":
        cantidad_producto = int(input("Cantidad de productos que vende la fonda: "))

        i = 1
        producto_fonda=0
        while cantidad_producto >= i:
            producto1 = input("Nombre producto " + str(i) + ":")
            precio1 = int(input("Precio " + producto1+":" ))

            if producto1 == producto:
                precio_suma=precio1
                cant_fondas+=1
                if precio1<precio_menor:
                    precio_menor=precio1
                    nombre_menor=fonda
                elif precio1>precio_mayor:
                    precio_mayor=precio1
                    nombre_mayor=fonda
            i += 1
    else:
        corte = False
if precio_suma==0:
    print("No existen datos para generar el rango de precios")
else:
    rango=precio_mayor-precio_menor
    print("El rango de precio para el producto ",producto," es $",rango)
    print("La fonda que lo vende más barato es:",nombre_menor,"a",precio_menor)
    print("La fonda que lo vende más caro es:",nombre_mayor,"a",precio_mayor)
    print("El producto se vende en",cant_fondas,"fondas")

