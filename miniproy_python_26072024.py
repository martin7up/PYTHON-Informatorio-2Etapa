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

import os

os.system('cls') 


script_dir = os.path.dirname(os.path.abspath(__file__))
print("Mi ubicacion es :", script_dir)


with open('documento_texto_miniproy.txt', 'r') as documento :
    texto = documento.read()

#----------------------------------------------------------------------------------------------------------------------------------------------
#Limpieza del texto
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace(';','')
texto = texto.lower()
lista_texto = texto.split(None)
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Obtencion de frecuencias empleando casteo a set y metodo de la clase str

texto_no_repetido = set(lista_texto)

for palabra in texto_no_repetido :
    print(f'La palabra [{palabra}] aparece {texto.count(palabra)} veces en el texto.')
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Obtencion de frecuencias empleando ciclos

cont = 0
aux = lista_texto[0]
lista_texto.sort()

for palabra in lista_texto : 
    if palabra == aux :
        cont += 1
    else :
        print(f'La palabra ({aux}) aparece un total de {cont} veces.')
        aux = palabra
        cont = 1
print(f'La palabra ({aux}) aparece un total de {cont} veces.')
#----------------------------------------------------------------------------------------------------------------------------------------------