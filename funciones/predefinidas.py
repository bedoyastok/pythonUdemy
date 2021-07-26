nombre = "daniel"

#funciones generales
print(type(nombre))#tipo de dato

#detectar el tipo isinstance
comprobar = isinstance(nombre,str)
if comprobar:
    print("variable tipo string")
else:
    print("No es string")

#eliminar espacios
frase = "    hola    "
print(frase)
print(frase.strip())#funcion para limpiar espacios

#eliminar variables
year = 2022
print(year)
del year
#print(year)

#contar caracteres
texto = "hola"
print(len(texto))

#encontrar caracteres
frase = "la vida es bella"
print(frase.find("vida"))

#reemplazar palabras
nuevaFrase = frase.replace("vida","moto")
print(nuevaFrase)

#mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())