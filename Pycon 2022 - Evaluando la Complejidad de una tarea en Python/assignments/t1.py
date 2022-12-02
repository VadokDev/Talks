from random import randint
from math import sqrt

billete1 = int(input("Denominación billete 1: P$ "))
billete2 = int(input("Denominación billete 2: P$ "))
moneda = int(input("Denominación moneda: P$ "))
presupuestoRandom = randint(100000, 1000000)
print("Monto inicial: P$",presupuestoRandom)

print("")

#Producto 1

nombreProducto = input("Nombre producto 1: ")
print("Ingrese el valor",nombreProducto,"(ecológico y extranjero)")
precio = int(input("P$ "))
cantUni = int(input("Ingrese cantidad de unidades: "))
vSinImpuestos = precio * cantUni
print("Valor total antes de impuestos: P$",vSinImpuestos)
print("Impuestos",nombreProducto,":")

precioExtranjero = round(vSinImpuestos - ((vSinImpuestos/980) * sqrt(vSinImpuestos)))
print("Extranjero: P$",precioExtranjero)

extraccion = vSinImpuestos%100
n1 = str(extraccion%10)
n2 = str(extraccion//10)
numeroInvertido = int(n1 + n2)
precioEcologico1 = round((numeroInvertido/100) * ((vSinImpuestos*20)/100))
print("Ecológico: P$",precioEcologico1)

precioTotalp1 = vSinImpuestos + precioEcologico1 + precioExtranjero
print("Valor total con impuestos: P$",precioTotalp1)

print(precioTotalp1//billete1,"billetes de P$",billete1)
print((precioTotalp1%billete1)//billete2,"billetes de P$",billete2)
print((precioTotalp1%billete1)%billete2//moneda,"monedas de P$",moneda)
print(((precioTotalp1%billete1)%billete2)%moneda//1,"monedas de P$ 1")
presupuestoRestante = presupuestoRandom - precioTotalp1
print("Presupuesto restante: P$",presupuestoRestante)

print("")

#Producto 2

nombreProducto = input("Nombre producto 2: ")
print("Ingrese valor",nombreProducto,"(1era. necesidad y ecológico)")
precio = int(input("P$ "))
cantUni = int(input("Ingrese cantidad de unidades: "))
vSinImpuestos = precio * cantUni
print("Valor total antes de impuestos: P$",vSinImpuestos)
print("Impuestos",nombreProducto,":")

precio1eraNecesidad = round((vSinImpuestos * 19)/100)
print("1era necesidad: P$",precio1eraNecesidad)

extraccion = vSinImpuestos%100
n1 = str(extraccion%10)
n2 = str(extraccion//10)
numeroInvertido = int(n1 + n2)
precioEcologico2 = round((numeroInvertido/100) * ((vSinImpuestos*20)/100))
print("Ecológico: P$",precioEcologico2)
precioTotal = vSinImpuestos + precio1eraNecesidad + precioEcologico2
print("Valor total con impuestos: P$",precioTotal)

print(precioTotal//billete1,"billetes de P$",billete1)
print((precioTotal%billete1)//billete2,"billetes de P$",billete2)
print((precioTotal%billete1)%billete2//moneda,"monedas de P$",moneda)
print(((precioTotal%billete1)%billete2)%moneda//1,"monedas de P$ 1")
print("Presupuesto restante: P$",presupuestoRestante - precioTotal)
print("")
print("Total pagado en impuestos: P$",precioExtranjero + precioEcologico1 + precioEcologico2 + precio1eraNecesidad)
print("Ecológico: P$",precioEcologico1 + precioEcologico2)
print("Extranjero: P$",precioExtranjero)
print("Primera necesidad: P$",precio1eraNecesidad)
