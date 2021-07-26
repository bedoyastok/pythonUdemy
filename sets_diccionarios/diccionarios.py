#tipo de dato que almacena clave valor

persona = {
    'nombre':'daniel',
    'apellido':'bedoya'
}

print(persona)

print(persona['apellido'])#accder a un valor por medio de la clave

#lista con diccionarios

contactos = [
    {
        'nombre':'antonio',
        'correo':'antonio@correo.com'
    },
    {
        'nombre':'luis',
        'correo':'luis@correo.com'
        
    },
    {
        'nombre':'salvador',
        'correo':'salvador@correo.com'
    }
]

print(contactos[1]['correo'])#obtenr dato con el indice del diccionario y la clave

contactos[1]['correo'] = 'no tengo'#modificar valor
print(contactos[1]['correo'])

for contacto in contactos:
    print('nombre del contacto es',contacto['nombre'])
    print('el correo es',contacto['correo'])
    print('------------------------------')