#variable global, para todas las funciones
frase = "global hola mundo"

def holaMundo():
    frase = "hola mundo"#variable solo dentro de esta funcion
    print("dentro de la funcion",frase)

    global year#convertir esta variable en global
    year = "2021"

    return frase,"en el año",year

print(holaMundo())

print("fuera de la funcion:",frase)#imprime la frase global
print("fuera de la funcion:",year)#imprime la variable convertida en global