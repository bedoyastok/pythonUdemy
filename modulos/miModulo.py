def saludo(nombre):
    return 'hola como estas',nombre

def calculadora(num1,num2,basicas=False):
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    resultado = ''

    if basicas != False:
        resultado += 'suma: ' + str(suma)
        resultado += '\n'
        resultado += 'resta: ' + str(resta)
        resultado += '\n'
    else:
        resultado += 'multiplicacion: ' + str(mult)
        resultado += '\n'
        resultado += 'division: ' + str(div)
        resultado += '\n'
    return resultado
