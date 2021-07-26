#definir una lista
peliculas = ["batman","spiderman","superman"]#opcion1
cantantes = list(("2pac","drake","fonseca"))#opcion2
years = list(range(2020,2050))
variada = ["victor",5,4.5,True]

""" print(peliculas)
print(cantantes)
print(years)
print(variada) """

#indices
""" print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:]) """

#añadir elementos a una lista
peliculas.append("flash")
cantantes.append("hector")

""" print(peliculas)
print(cantantes) """

#insertar nuevos elementosa la lista con un while
""" nueva_pelicula = ""
while nueva_pelicula != "no":
    nueva_pelicula = input("introduce la nueva pelicula: ")

    if nueva_pelicula != "no":
        peliculas.append(nueva_pelicula)

#recorrer lista
for pelicula in peliculas:
    #print(pelicula)
    print("numero",peliculas.index(pelicula)+1,pelicula,) """

#listas multidimensionales o listas dentro de otras listas
contactos = [
    [
        'antonio',
        'antonio@correo.com'
    ],
    [
        'luis',
        'luis@correo.com'
    ],
    [
        'salvador',
        'salvador@correo.com'
    ]
]

print(contactos[1][1])#acceder a diferentes datos por medio del indice

for contacto in contactos:
    print(contacto[0])#asi recorre e imprime solo los nombre de cada lista


for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print('nombre: ',elemento)
        else:
            print('email: ',elemento)
    print('\n')