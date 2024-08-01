#Consigna : Crear un juego para 2 participantes, en el cual deban intentar adivinar,por turnos, un numero del 0 al 9.

import random
import time
import os

aciertos_jugador1 = dict()
aciertos_jugador2 = dict()

num_adivinado1 = None
num_adivinado2 = None
valor_generado = None

for turno in range(0, 2):
    
    os.system('cls')

    print(f'Turno numero {turno}')
    num_adivinado1 = int(input(f'Jugador 1; ingrese un numero : >>> '))
    valor_generado = random.randint(0, 10)
    
    if num_adivinado1 == valor_generado:
        print('Felicidades jugador 1, acerto!')
        aciertos_jugador1[num_adivinado1] = valor_generado
    else :
        print('No adivinaste correctamente!')
        aciertos_jugador1[num_adivinado1] = valor_generado

    time.sleep(2)
    os.system('cls')

    #Se repite lo mismo que el anterior bloque pero ahora para el jugador 2
    print(f'Turno numero {turno}')
    num_adivinado2 = int(input(f'Jugador 2; ingrese un numero : >>> '))
    valor_generado = random.randint(0, 10)
    
    if num_adivinado2 == valor_generado:
        print('Felicidades jugador 2, acerto!')
        aciertos_jugador2[num_adivinado2] = valor_generado
    else :
        print('No adivinaste correctamente!')
        aciertos_jugador2[num_adivinado2] = valor_generado
     
    time.sleep(2)

os.system('cls')
print('Fin del juego!...')

print('\nResultados jugador 1')
for k,v in aciertos_jugador1.items():
    print(f'Valor adivinado : {k} <<>> Valor generado : {v} >>>', 'Acerto.' if k==v else 'No acerto.')

print('\nResultados jugador 2')
for k,v in aciertos_jugador2.items():
    print(f'Valor adivinado : {k} <<>> Valor generado : {v} >>>', 'Acerto.' if k==v else 'No acerto.')