def traducir_tipo(tipo):
    result = None
    if tipo == list:
        result = 'Lista'
    elif tipo == str:
        result = 'Texto'
    elif tipo == int:
        result = 'Numero'
    elif tipo == bool:
        result = 'Booleano'    
    return result

def comprobar_tipado(dato,tipo):
    test = isinstance(dato,tipo)
    result = ''

    if test:
        result = 'dato tipo: ',traducir_tipo(tipo)
    else:
        result = 'este tipo no coincide'

    return result

mi_list = ['hola',1]
titulo = 'ingeniero'
numero = 100
verdadero = True

print(comprobar_tipado(mi_list,type(mi_list)))
print(comprobar_tipado(titulo,type(titulo)))
print(comprobar_tipado(numero,type(numero)))
print(comprobar_tipado(verdadero,type(verdadero)))