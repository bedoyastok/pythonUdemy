nombre = input("ingresa nombre: ")
apellidos = input("ingresa apellido: ")

def getNombre(nombre):    
    texto = "Hola, tu nombre es",nombre,"y"
    return texto

def getApellido(apellidos):
    texto = "Tu apellido es",apellidos
    return texto

def getAll(nombre,apellidos):
    texto = getNombre(nombre),getApellido(apellidos)
    return texto


print(getAll(nombre,apellidos))