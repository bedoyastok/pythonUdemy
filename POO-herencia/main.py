import clases

persona = clases.Persona()
persona.setNombre('daniel')
persona.setApellidos('bedoya')
persona.setAltura('174 cm')
persona.setEdad('30 años')

print(' Mi nombre completo es',persona.getNombre(),
      persona.getApellidos(),'\n',
      'Tengo',persona.getEdad(),'\n',
      'Mi altura es de',persona.getAltura())
print(persona.hablar())

print('\n********************\n')

informatico = clases.Informatico()
informatico.setNombre('oscar')
informatico.setApellidos('barajas')

print('el informatico es',informatico.getNombre(),
      informatico.getApellidos())
print(informatico.getlenguajes())

print('\n********************\n')

tecnico = clases.TecnicoRedes()
tecnico.setNombre('manolo')
print(tecnico.auditarRedes,#variable del constructor
      tecnico.getNombre(),#se le asigna de la clase padre
      tecnico.getlenguajes())#se usa al invocar el constructor