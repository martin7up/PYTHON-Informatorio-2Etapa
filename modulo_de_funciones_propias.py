from pathlib import Path
import time
import os

#----------------------------------------------------------------------------------------------------------------------------------------------
#Devuelve True si una cadena representa un Real
def es_numero_real(cadena : str) -> bool: 
    
    return cadena.isnumeric() or (cadena.count('.') == 1 and cadena.replace('.','1',1).isnumeric())#Cortocircuito por True 
#print(es_numero_real(input('Valor : ')))
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Devuelve una cadena que solo contiene letras
def limpiar_texto(texto : str = None, dejar_numeros : bool = False, dejar_espacios : bool = True) -> str: 
    
    if not texto: #Si el texto es None se interpreta como falso, se niega, y por lo tanto se ejecuta el retorno None
        return None 
    if texto.isspace():
        return None
    
    texto = (texto.lower()).strip()
    texto_no_repetido = set(texto)

    if dejar_numeros == False and dejar_espacios == True : 
        for caracter in texto_no_repetido : 
            if not(caracter.isalpha() or caracter == '\n' or caracter.isspace()) :
                texto = texto.replace(caracter,'')
        return texto                                     
    elif dejar_numeros == True and dejar_espacios == False:
        for caracter in texto_no_repetido : 
            if not(caracter.isalnum() or caracter == '\n') :
                texto = texto.replace(caracter,'')
        return texto
    elif dejar_numeros == False and dejar_espacios == False:
        for caracter in texto_no_repetido : 
            if not(caracter.isalpha() or caracter == '\n') :
                texto = texto.replace(caracter,'')
        return texto                              
    else : 
        for caracter in texto_no_repetido : 
            if not(caracter.isalnum() or caracter == '\n' or caracter.isspace()) :
                texto = texto.replace(caracter,'')
        return texto              
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Devuelve una lista limpia de palabras
def desmenuzar_en_palabras_simples(texto : str = None, dejar_numeros : bool = False) -> list:
    
    return limpiar_texto(texto, dejar_numeros).split(None) if texto is not None else None
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Insiste en el ingreso de una cadena cuyos caracteres sean solo letras, devuelve una cadena limpia de caracteres que no sean exclusivamente letras
def ingreso_cadena_de_letras(limpiar : bool = False ,mensaje : str = 'Ingrese solamente letras : >>> ') -> str:
    
    while True :
        cadena = input(f'\n\n{mensaje}').strip()
        if str.isalpha(cadena) :
            return cadena if limpiar else limpiar_texto(cadena)
        else :
            print('Parece que ha ingresado texto que contiene caracteres que no son alfabeticos.')
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Funcion de espera
def funcion_de_espera(lapso : int = 3, mensaje : str = 'En : ') -> None:
    
    for instante in range(lapso, 0,-1):
        print(f'{mensaje} {instante}')
        time.sleep(1)
        os.system('cls')
    return 
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Apertura del documento a analizar
def abrir_un_documentotxt_imprimir(mensaje : str = 'Ingrese a continuacion la ruta absoluta del documento >>> ') -> str:

    ruta = input(mensaje)
    
    if Path(ruta).exists() and Path(ruta).is_file() and Path(ruta).suffix == '.txt':
        with open(ruta, 'r') as documento :
            return documento.read()    
    else : 
        return None
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Funcion es palindromo
def es_palindromo(lista : list) ->bool:
    
    if not lista: return None

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

#----------------------------------------------------------------------------------------------------------------------------------------------
#Obtencion de frecuencias empleando ciclos, a partir de una lista que contiene strings
def frecuencias_palabras_en_texto(lista : list) -> tuple:

    if not lista: return None

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
    
    conjunto_palabra_frecuencia = dict(reversed(sorted(conjunto_palabra_frecuencia.items(), key=lambda item: len(item[0]))))#Ordenar palabras por longitud de cadena

    estadisticas['ESTADISTICA >>> TOTAL DE PALABRAS : '] = len(lista)
    estadisticas['ESTADISTICA >>> PALABRA MAS LARGA : '] = max(lista, key=len)#Obtener la palabra de mayor longitud
    estadisticas['ESTADISTICA >>> PALABRA MAS CORTA : '] = min(lista, key=len)
    
    return (conjunto_palabra_frecuencia, estadisticas)
#----------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#Verificar si un string posee caracteres repetidos
def tiene_caracteres_repetidos(cadena : str = None) -> bool:
    
    if not cadena : 
        return None
    
    return len(set(cadena)) == len(cadena)
#----------------------------------------------------------------------------------------------------------------------------------------------