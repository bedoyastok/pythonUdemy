#importar modulo#
import sqlite3

#conexion de base de datos#
conexion = sqlite3.connect('pruebas.db')


#crear cursor#
cursor = conexion.cursor()


#crear tabla#
cursor.execute("""
               CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo VARCHAR(255),
                descripcion TEXT,
                precio INT(255))
               """)
#guardar cambios#
conexion.commit()



#insertar datos#
#cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripcion de mi producto', 550)")
#guardar cambios#
#conexion.commit()



#borrar registros#
#cursor.execute("DELETE FROM productos")
#conexion.commit()



#insertar muchos registros#
productos = [
    ("computador","descripcion del computador",1000),
    ("carro","descripcion del carro",10),
    ("cacharro","descripcion del cacharro",1000),
    ("moto","descripcion de la moto",10)
    ]
cursor.executemany('''INSERT INTO productos VALUES(null,?,?,?)''',productos)
conexion.commit()



#Update#
cursor.execute("UPDATE productos SET precio=666 WHERE precio=10")
conexion.commit()



#borrar registros#
#cursor.execute("DELETE FROM productos")
#conexion.commit()



#listar datos#
cursor.execute("SELECT * FROM productos")
#obtener filas#
productos = cursor.fetchall()

#print(productos)

for producto in productos:
    print(producto)
    print('\n id del producto:',producto[0])
    print('\n nombre del producto:',producto[1])
    print('*****************************')



#cerrar conexion db#
conexion.close()
