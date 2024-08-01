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
def limpiar_texto(texto : str = None, dejar_numeros : bool = False) -> str: 
    
    if not texto: #Si el texto es None se interpreta como falso, se niega, y por lo tanto se ejecuta el retorno None
        return None 
    if texto.isspace() == True: 
        print('RETORNO UN VACIO 2')
        return None
    
    texto = (texto.lower()).strip()
    texto_no_repetido = set(texto)

    '''Esta segmento elimina del texto todo excepto letras, espacio y salto de linea; numeros se eliminan por defecto pero se puede cambiar en parametros'''
    if dejar_numeros: #De esta manera se hace una sola vez la comprobacion, si se coloca dentro del ciclo se comprueba en vano en cada pasada
        for caracter in texto_no_repetido : 
            if not(caracter.isalnum() or caracter is '\n' or caracter.isspace()) :
                texto = texto.replace(caracter,'')
    else :
        for caracter in texto_no_repetido : 
            if not(caracter.isalpha() or caracter is '\n' or caracter.isspace()) :
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