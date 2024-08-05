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
from modulo_de_funciones_propias import abrir_un_documentotxt_imprimir as abrir
from modulo_de_funciones_propias import tiene_caracteres_repetidos as caracteres
from modulo_de_funciones_propias import desmenuzar_en_palabras_simples as desmenuzar
from modulo_de_funciones_propias import frecuencias_palabras_en_texto as estadisticas
#from itertools import chain

#Info del documento ejecutado------------------------------------------------------------------------------------------------------------------
os.system('cls') 
print("EL programa que esta ejecutando se encuentra ubicado en :", os.path.dirname(os.path.abspath(__file__)))

#Cuerpo principal del programa-----------------------------------------------------------------------------------------------------------------

print('\n')

texto = abrir()

print(texto if texto is not None else 'Algo salio mal con la lectura...')

lista_texto = desmenuzar(texto)

tupla_de_datos = estadisticas(lista_texto)

print('\n')

for k,v in tupla_de_datos[0].items():
    print(f'Palabra : [{k}];    Frecuencia : {v}')

print('\n')

for k,v in tupla_de_datos[0].items():
    if caracteres(k) :
        print(k, ' es la palabra de mayor longitud y que primero aparece en la lista, cuyos caracteres son todos distintos.')
        break

print('\n')

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