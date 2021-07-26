numeros = [45,545,22,49,65,262,89]

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += 'elemento:'+ str(elemento)
        resultado += '\n'
    return resultado

print('-------recorrer y leer---------')
#for numero in numeros:
#    print(numero)

print(mostrarLista(numeros))
