import mysql.connector

#conexion#
database = mysql.connector.connect(
    host     = 'localhost',
    user     = 'root',
    password = 'mysql',
    database = 'master_python'
    )

#comprobar conexion#
#print(database)

#cursor para ejecutar las consultas#
cursor = database.cursor()

# =============================================================================
# cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
# 
# cursor.execute("SHOW DATABASES")
# 
# for bd in cursor:
#     print(bd)
# =============================================================================
    
    
#crear tablas#
cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos
               (id int(10) auto_increment not null,
                marca varchar(40) not null,
                modelo varchar(40) not null,
                precio float(10,2) not null,
                CONSTRAINT pk_vehiculo PRIMARY KEY(id))  
               """)
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
    
#cursor.execute("INSERT INTO vehiculos VALUES(null,'opel','astra',15888)")

# =============================================================================
# coches = [
#     ('seat','ibiza',5000),
#     ('renault','clio',6500),
#     ('citroen','cuarzo',8000),
#     ('mazda','triple',5660)
#     ]
# cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)
# =============================================================================
database.commit()


cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

for coche in result:
    print(coche,"imprime toda la fila\n")
    print('-----------')
    print('\n id del coche:',coche[0])
    print('\n nombre del coche:',coche[1])
    print('*****************************')

cursor.execute("DELETE FROM vehiculos WHERE marca = 'opel'")
database.commit()
print('\n',cursor.rowcount,"datos borrados!!!!***")



cursor.execute("UPDATE vehiculos SET modelo = 'leon' WHERE marca = 'seat'")
database.commit()
print('\n',cursor.rowcount,"datos actualizados!!!!***")






