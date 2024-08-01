import random
import time
import os

aciertos_jugador1 = dict()
aciertos_jugador2 = dict()

num_adivinado1 = None
num_adivinado2 = None
valor_generado = None


for turno in range(0, 2):
    print(f'Turno numero {turno}')
    num_adivinado1 = input(f'Jugador 1; ingrese un numero : >>> ')    
    valor_generado = random.randint(0, 10)
    if num_adivinado1 == valor_generado:
        print('Felicidades jugador 1, acerto!')
        aciertos_jugador1[num_adivinado1] = valor_generado
    else :
        print('No adivinaste correctamente!')
        aciertos_jugador1[num_adivinado1] = valor_generado

    time.sleep(2)
    os.system('cls')

    print(f'Turno numero {turno}')
    num_adivinado2 = input(f'Jugador 2; ingrese un numero : >>> ')
    valor_generado = random.randint(0, 10)
    if num_adivinado2 == valor_generado:
        print('Felicidades jugador 2, acerto!')
        aciertos_jugador2[num_adivinado2] = valor_generado
    else :
        print('No adivinaste correctamente!')
        aciertos_jugador2[num_adivinado2] = valor_generado
     
    time.sleep(2)
    os.system('cls')

print('Fin del juego!... Los resultados son : >>> ')

print('Resultados jugador 1')
for k,v in aciertos_jugador1.items():
    print(f'Valor adivinado : {k}; Valor generado : {v}')

print('Resultados jugador 2')
for k,v in aciertos_jugador2.items():
    print(f'Valor adivinado : {k}; Valor generado : {v}')
