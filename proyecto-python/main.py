from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hacerEl = acciones.Acciones()

accion = input("Escribe tu opcion: ")

if accion == "registro":
    hacerEl.registro()

elif accion == "login":
    hacerEl.login()