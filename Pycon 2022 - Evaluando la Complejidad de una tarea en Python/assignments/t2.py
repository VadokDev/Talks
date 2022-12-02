# PREGUNTAS
horas_est= int(input("Ingresa horas de estudio: "))

# CANTIDAD INICIAL DE PUNTOS
if horas_est < 5:
    promedio_tri = int(input("Ingresa promedio del trimestre anterior: "))
    if promedio_tri < 55:
        puntaje = -30
    elif promedio_tri < 80:
        puntaje = 0
    else:
        puntaje = 10
elif horas_est <= 9:
    puntaje = 15
elif horas_est <= 19:
    puntaje = 20
else:
    puntaje = 30

respuesta1 = input("¿Tuviste evaluaciones esta semana? (si/no): ")
if respuesta1 == "si":
    promedio_sem = int(input("Promedio de evaluaciones: "))
    
# CAMBIO DE PUNTAJE SEGUN PROMEDIO SEMANAL
if respuesta1 == "si":
    if promedio_sem < 55:
        puntaje = puntaje - abs(puntaje)*0.2
        if horas_est >= 5:
            promedio_tri = int(input("Ingresa promedio del trimestre anterior: "))
        if promedio_tri < 55:
            puntaje -= 10
    elif promedio_sem < 80:
        puntaje = puntaje + abs(puntaje)*0.1
    elif promedio_sem < 89:
        puntaje = puntaje + abs(puntaje)*0.15
    else:
        puntaje = puntaje + abs(puntaje)*0.20 + 30

respuesta2 = input("¿Ayudaste en tareas de la casa? (si/no): ")
if respuesta2 == "si":
    horas_ayuda = int(input("Ingresa horas de ayuda: "))
# CAMBIO DE PUNTAJE SEGUN TAREAS DOMÉSTICAS
if respuesta2 == "si":
     puntaje = puntaje + abs(puntaje)*0.20 + 2*horas_ayuda
else:
     puntaje = puntaje - abs(puntaje)*0.1

# RESULTADO
print("Obtuviste", puntaje, "puntos.")
if puntaje <= 0:
    print("No hay tiempo de juego esta semana.")
elif puntaje < 10:
    juego = round(0.3*puntaje)
    print("Debes esforzarte un poco más. Puedes jugar hasta", juego,"horas esta semana.")
elif puntaje < 20:
    juego = round(0.5*puntaje)
    print("Puedes jugar hasta", juego, "horas esta semana.")
else:
    print("¡¡¡Excelente trabajo!!!")
    if puntaje <= 30:
        print("Puedes jugar hasta", round(puntaje), "horas esta semana.")
    else:
        print("Puedes jugar hasta 30 horas esta semana.")


        
    
