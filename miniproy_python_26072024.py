# Descripción del Proyecto:

#   Desarrollar un programa en Python que lea un archivo de texto y realice las siguientes tareas:
#   Contar el número total de palabras.
#   Encontrar la palabra más frecuente y su frecuencia.
#   Determinar si el texto es un palíndromo palabra por palabra (ignorar espacios y puntuaciones).
#   Calcular la longitud de la subcadena más larga sin caracteres repetidos.
#   Generar una tabla de frecuencia de las palabras y mostrar las 10 palabras más comunes.

# Requisitos:

#   El programa debe manejar correctamente los archivos de texto.                                                 -> X
#   El programa debe ignorar las mayúsculas y minúsculas en el conteo de palabras.
#   El programa debe ignorar la puntuación en todas las tareas.

# Asignación de Roles:

#   Líder del Grupo: Coordina el trabajo del equipo, asegura que todos los miembros entiendan las tareas y organiza las reuniones.
#   Desarrollador Principal: Encargado de escribir la mayor parte del código, pero debe trabajar en estrecha colaboración con los demás.
#   Encargado de Pruebas: Desarrolla casos de prueba para asegurar que el código funcione correctamente, detecta y corrige errores.
#   Documentador: Se encarga de escribir los comentarios y la documentación del código, explica las decisiones tomadas.
#   Presentador: Prepara y presenta el trabajo final del grupo al resto de la clase.


#Importaciones necesarias----------------------------------------------------------------------------------------------------------------------
import os
import time
from pathlib import Path
from modulo_de_funciones_propias import funcion_de_espera as banca
from modulo_de_funciones_propias import abrir_un_documentotxt_imprimir as abrir
from modulo_de_funciones_propias import desmenuzar_en_palabras_simples as desmenuzar
#from itertools import chain

#Info del documento ejecutado------------------------------------------------------------------------------------------------------------------
os.system('cls') 
print("EL programa que esta ejecutando se encuentra ubicado en :", os.path.dirname(os.path.abspath(__file__)))

#Obtencion de frecuencias empleando ciclos-----------------------------------------------------------------------------------------------------
def frecuencias_palabras_en_texto(lista : list) -> tuple:

    cont = 0
    aux = lista[0]
    lista.sort()
    conjunto_palabra_frecuencia = dict()
    estadisticas = dict()
    
    for palabra in lista : 
        if palabra == aux :
            cont += 1
        else :# Ver uso de else como fin rregular de un ciclo.
            conjunto_palabra_frecuencia[aux] = cont
            aux = palabra
            cont = 1
    conjunto_palabra_frecuencia[aux] = cont
    
    conjunto_palabra_frecuencia = dict(sorted(conjunto_palabra_frecuencia.items(), key=lambda item: item[1]))

    estadisticas['ESTADISTICA >>> TOTAL DE PALABRAS : '] = len(lista)
    estadisticas['ESTADISTICA >>> PALABRA MAS LARGA : '] = max(lista)
    estadisticas['ESTADISTICA >>> PALABRA MAS CORTA : '] = min(lista)
    
    return (conjunto_palabra_frecuencia, estadisticas)
#----------------------------------------------------------------------------------------------------------------------------------------------

#Funcion es palindromo-------------------------------------------------------------------------------------------------------------------------
def es_palindromo(lista : list) ->bool:

    if len(lista)%2 == 0:
        print('PAR')
        for indice in range(0, int(len(lista)/2)):
            print(f'{lista[indice]} - {lista[-indice-1]}')
            if lista[indice] != lista[-indice-1] :
                return False
        return True
    else :
        print('IMPAR')
        for indice in range(0, int((len(lista)-1)/2)): #Aqui primero restar 1 a la longitud, luego dividir; caso contrario falla por truncado
            print(f'{lista[indice]} - {lista[-indice-1]}')
            if lista[indice] != lista[-indice-1] :
                return False
        return True
#----------------------------------------------------------------------------------------------------------------------------------------------


#Cuerpo principal del programa-----------------------------------------------------------------------------------------------------------------

texto = abrir()

print(texto if texto is not None else 'Algo salio mal con la lectura...')

lista_texto = desmenuzar(texto)

tupla_de_datos = frecuencias_palabras_en_texto(lista_texto)

for k,v in tupla_de_datos[0].items():
    print(f'Palabra : {k}; Frecuencia : {v}')

for k,v in tupla_de_datos[1].items():
    print(k,v)

#----------------------------------------------------------------------------------------------------------------------------------------------


#Borradores------------------------------------------------------------------------------------------------------------------------------------
#'''Primer intento, hay que especificar que eliminar.'''
# texto = ((texto.replace(',','')).replace('.','')).replace(';','')
#  
#'''Segundo intento, pero lo que se elimina sigue siendo limitado, y de yapa ascii puso de manera no continua los valores para simbolos de puntuacion'''
# for codigo_ascii in chain(range(33,48) and range(58, 65) and range(91,97) and range(123, 127)): 
#     texto.replace(chr(codigo_ascii),'')

#Obtencion de frecuencias empleando casteo a set y metodo de la clase str(no resulto de manera correcta)
# texto_no_repetido = set(lista_texto)
# for palabra in texto_no_repetido :
#     print(f'La palabra [{palabra}] aparece {texto.count(palabra)} veces en el texto.')

#Version con opciones de menu para Programa main
# print('Menu.\n1 >>> Crea un archivo de texto.\n2 >>> Mostrar los archivos disponibles.\n3 >>> Modificar un archivo.'+
#       '\n4 >>> Eliminar un archivo de texto.\n5 >>> Mostrar un archivo de texto.\n6 >>> Salir.')
# opcion = None
# while not ((opcion := input('Opcion seleccionada ¿? : >>> ')).isdigit() and len(opcion)== 1 and int(opcion) in range(1,7)) :
#     os.system('cls')
#     funcion_de_espera(4, 'Algo salio mal intente nuevamente en :')
# print(f'Opcion selecionada : {opcion}')
#---------------------------------------------------------------------------------------------------------------------------------------------