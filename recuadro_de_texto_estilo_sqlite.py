cadena_a_encuadrar = 'Mariano Aranaud, es alguien\nque me acabo de inventar.'
print(cadena_a_encuadrar)

cadena_a_encuadrar = cadena_a_encuadrar.splitlines()

print(len(max(cadena_a_encuadrar))*'- ')
for linea in cadena_a_encuadrar:
    print(linea)