'''Practicas realizadas en clases'''
# print('Hola chamigo!')
# numero = int (input("Ingrese un valor ... "))
# print(numero)

'''Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla'''

#Alternativa perezosa:
#print('El nombre ingresado es :',input('Ingrese su nombre a continuacion : '))

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

def es_numero_real(cadena : str) -> bool: 
    return cadena.isnumeric() or (cadena.count('.') == 1 and cadena.replace('.','1',1).isnumeric())#Cortocircuito por True 

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

'''Crea un programa que pida al usuario elr adio de un circulo y calcule su area.'''

# PI = 3.1416
# radio = float (input('Ingrese el radio del circulo para calcular el perimetro, area y volumen(esfera) ¿? : >>> ').strip())
# print(f'El perimetro es : {2*PI*radio:.4f} u.m.\nEl area es : {PI*radio**2:.4f} u.m.^2\nLa volumen (esfera 3D) : {(4/3)*PI*radio**3:.4f} u.m.^3')

'''Escribe un programa que pida la base y altura de un triangulo Isoceles y retorne su area por pantalla.'''
# := operador walrus... cortesia de GPT.

# base = 0
# altura = 0
# print('Calcular el area de un triangulo Isoceles.')
# bandera = False
# while bandera := not es_numero_real( base := input('Ingrese un numero real ¿? : >>> ' if not bandera else '...algo salio mal; intente de nuevo : >>> ').strip()) : 
#     pass 
# print('El valor ingresado para la base es :', base := float(base))

# bandera = False
# while bandera := not es_numero_real( altura := input('Ingrese un numero real ¿? : >>> ' if not bandera else '...algo salio mal; intente de nuevo : >>> ').strip()) : 
#     pass 
# print('El valor ingresado para la altura es :', altura := float(altura), f'\nEl area total del triangulo Iso es : {base}*{altura}/2 = {(base*altura/2):.4f}')

'''Crea un programa que pida al usuario una cantidad en dolares y la convierta a euros 0.84eu/uss'''

#print(f'La cantidad correspondiente en euros es : >>> {float (input('Ingrese la cantidad en dolares ¿? : >>> ').strip())*0.84:.2f}')

'''Crea un programa que pida al usuario una palabra y muestr en pantalla cuantas letras tiene.'''

#print(f'La cantidad de caracteres en la frase ingresada es : >>> {len(input('Ingrese una frase ¿? : >>> ').strip())}')

'''Escribe un programa que solicite al usuario su fecha de nacimiento en fomrato dd/mm/aaaa y luego imprima su edad en anios.'''

fecha_actual = input('Fecha actual (dd/mm/aaaa) ¿? : >>> ')
fecha_nacimiento = input('Fecha de nacimiento (dd/mm/aaaa) ¿? : >>> ')

print(f'Edad aproximada : >>> {int (fecha_actual.split('/')[2])- int (fecha_nacimiento.split('/')[2])}')
