import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nPerfecto, vamos a registrate...\n")
        nombre = input("Escribe tu nombre:")
        apellidos = input("Escribe tus apellidos:")
        email = input("Escribe tu correo:")
        contrasena = input("Escribe una contrasena:")

        usuario = modelo.Usuario(nombre,apellidos,email,contrasena)
        registro = usuario.registrar()

    def login(self):
        print("\nPerfecto, vamos a identificarte...")   
        email = input("Escribe tu correo:")
        contrasena = input("Escribe tu contrasena:") 