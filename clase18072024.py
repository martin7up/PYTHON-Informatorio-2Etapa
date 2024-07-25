'''Practicas realizadas en clases'''
# print('Hola chamigo!')
# numero = int (input("Ingrese un valor ... "))
# print(numero)

'''Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla'''

# while True :
#     nombre = input('\n\nEjercicio 1 >>> \nIngrese su nombre completo : >>> ').strip()
#     if str.isalpha(nombre) :
#         print('El nombre ingresado es : ',nombre)
#         break
#     else :
#         print('Parece que ha ingresado texto que contiene caracteres que no son alfabeticos.')

'''Escribe un programa que solicite al usuario su nombre y luego imprima un mensaje de bienvenida'''

# while True :
#     nombre = input('\n\nEjercicio 2 >>> \nIngrese su nombre completo : >>> ').strip()
#     if str.isalpha(nombre) :
#         print('Biemvenido ',nombre,'!!!')
#         break
#     else :
#         print('Parece que ha ingresado texto que contiene caracteres que no son alfabeticos.')

'''Escribe un programa que solicite al usuario su edad y luego lo imprima en pantalla'''

# while True :

#     nombre = input('\n\nEjercicio 3 >>> \nIngrese su nombre completo : >>> ').strip()

#     if str.isalpha(nombre) :       
#         nombre = input(f'{nombre}, prodria porfavor ingresar su edad en anio (ejemp : 27) : >>> ').strip() #Solo para mostrar el tipado dinamico en Python

#         if nombre.isnumeric(): 
#             nombre = int(nombre)      
#             print(f'La edad ingresada es : {nombre}')
#             break
#         else :
#             print('Parece que ha ingresado algo caracteres que no son numero; intente de nuevo.')
#     else :
#         print('Parece que ha ingresado texto vacio, o que contiene caracteres que no son alfabeticos.')

'''Escriba un programa que calcule la suma de dos numeros y la imprima en pantalla.'''

# def es_numero_real(cadena : str) -> bool: 
#     return num1.isnumeric() or (num1.count('.') == 1 and num1.replace('.','1',1).isnumeric())#Cortocircuito por True 

# while True :
     
#     num1 = input('Ingrese un numero cualquiera en formato real de no mas de 4 partes luego del pto fracc (ejemp : 9.0091) : ¿? >>> ').strip()
#     if es_numero_real(num1) :
#         num1 = float(num1)
#         break
#     else :
#         print('Parece que los caracteres ingresados no tienen el formato correcto; intente de nuevo...')

# while True :
     
#     num2 = input('Ingrese otro numero cualquiera en formato real de no mas de 4 partes luego del pto fracc (ejemp : 9.0091) : ¿? >>> ').strip()
#     if es_numero_real(num2) :
#         num2 = float(num2)
#         break
#     else :
#         print('Parece que los caracteres ingresados no tienen el formato correcto; intente de nuevo...')

# print(f'La suma {num1} + {num2} tiene por resultado : {num1 + num2}')