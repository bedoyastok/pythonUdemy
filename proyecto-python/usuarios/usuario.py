import mysql.connector

database = mysql.connector.connect(
    host        = 'localhost',
    user        = 'root',
    password    = 'mysql',
    database    = 'master_python',
    port        = 3306
)
#print(database)

cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self,nombre,apellidos,email,contrasena):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = contrasena

    def registrar(self):
        fecha = "01-01-2021"
        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre,self.apellidos,self.email,self.contrasena,fecha)

        cursor.execute(sql,usuario)
        database.commit()

        return[cursor.rowcount,self]

    def identificar(self):
        return self.apellidos
