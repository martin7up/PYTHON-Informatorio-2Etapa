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
#from itertools import chain
from pathlib import Path

#Info del documento ejecutado------------------------------------------------------------------------------------------------------------------
os.system('cls') 
print("Mi ubicacion es :", os.path.dirname(os.path.abspath(__file__)))

#Apertura del documento a analizar-------------------------------------------------------------------------------------------------------------
def abrir_un_documento() -> str:
    os.system('cls')

    ruta = input('Ingrese a continuacion la ruta absoluta del documento ')
    
    if Path.exists(ruta) and Path.is_file(ruta) and Path(ruta).suffix == '.txt':
        with open(ruta, 'r') as documento :
            return documento.read()    
    else : 
        return None
#----------------------------------------------------------------------------------------------------------------------------------------------

#Limpieza del texto----------------------------------------------------------------------------------------------------------------------------
def limpieza_de_texto(texto = None) -> list:
    if texto is None: return None
    
    texto = (texto.lower()).strip()
    texto_no_repetido = set(texto)

    '''Esta segmento elimina del texto todo excepto letras, espacio y salto de linea.'''
    for caracter in texto_no_repetido : 
        if not(caracter.isalpha() or caracter is '\n' or caracter.isspace()) :
            texto = texto.replace(caracter,'')    
    return texto.split(None)
#----------------------------------------------------------------------------------------------------------------------------------------------

#Obtencion de frecuencias empleando ciclos-----------------------------------------------------------------------------------------------------
def frecuencias_palabras_en_texto(lista : list) -> None:
    cont = 0
    aux = lista[0]
    lista.sort()
    
    for palabra in lista : 
        if palabra == aux :
            cont += 1
    else :
        print(f'La palabra ({aux}) aparece un total de {cont} veces.')
        aux = palabra
        cont = 1
    print(f'La palabra ({aux}) aparece un total de {cont} veces.')
    print(f'En total se identificaron unas {len(lista)} palabras.\nLa mayor es {max(lista)}.\nLa menor es {min(lista)}.')
#----------------------------------------------------------------------------------------------------------------------------------------------

#Funcion de espera-----------------------------------------------------------------------------------------------------------------------------
def funcion_de_espera(lapso : int = 3, mensaje : str = 'En : ') -> None:
    
    for instante in range(lapso, 0,-1):
        print(f'{mensaje} {instante}')
        time.sleep(1)
        os.system('cls')
    return 
#----------------------------------------------------------------------------------------------------------------------------------------------

#Cuerpo principal del programa-----------------------------------------------------------------------------------------------------------------
print('Menu.\n1 >>> Crea un archivo de texto.\n2 >>> Mostrar los archivos disponibles.\n3 >>> Modificar un archivo.'+
      '\n4 >>> Eliminar un archivo de texto.\n5 >>> Mostrar un archivo de texto.\n6 >>> Salir.')

opcion = None
while not ((opcion := input('Opcion seleccionada ¿? : >>> ')).isdigit() and len(opcion)== 1 and int(opcion) in range(1,7)) :
    os.system('cls')
    funcion_de_espera(4, 'Algo salio mal intente nuevamente en :')
print(f'Opcion selecionada : {opcion}')

texto = abrir_un_documento()
print(texto if texto is not None else 'Algo salio mal con la lectura...')
#----------------------------------------------------------------------------------------------------------------------------------------------

#Borradores------------------------------------------------------------------------------------------------------------------------------------
#'''Primer intento, hay que especificar que eliminar.'''
# texto = ((texto.replace(',','')).replace('.','')).replace(';','')
#  
#'''Segundo intento, pero lo que se elimina sigue siendo limitado, y de yapa ascii puso de manera no continua los valores para simbolos de puntuacion'''
# for codigo_ascii in chain(range(33,48) and range(58, 65) and range(91,97) and range(123, 127)): 
#     texto.replace(chr(codigo_ascii),'')
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Obtencion de frecuencias empleando casteo a set y metodo de la clase str(no resulto de manera correcta)
# texto_no_repetido = set(lista_texto)
# for palabra in texto_no_repetido :
#     print(f'La palabra [{palabra}] aparece {texto.count(palabra)} veces en el texto.')
#----------------------------------------------------------------------------------------------------------------------------------------------