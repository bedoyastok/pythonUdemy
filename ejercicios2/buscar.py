numeros = [45,545,22,49,65,262,89]

numBuscar = int(input('introduce un numero: '))

comprobar = isinstance(numBuscar,int)
while not comprobar or numBuscar <= 0:
    numBuscar = int(input('introduce el numero: '))
else:
    print('has instroducido el numero: ',numBuscar)

print('buscar en la lista el numero: ',numBuscar)

buscar = numeros.index(numBuscar)
print('el numero se encuentra en la posicion: ',buscar)
