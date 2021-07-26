""" import miModulo

nom = input('ingresa tu nombre: ')
print(miModulo.saludo(nom))

num1 = int(input('ingresa un numero: '))
num2 = int(input('ingresa otro numero: '))
print(miModulo.calculadora(num1,num2,True)) """
#-----------------------------------#
""" import datetime #importa todo y se debe llamar al datetime.class.metodo()
from datetime import * #asi no es necesario llamar el modulo solo class.metodo()

print(date.today())
fecha_completa = datetime.now()

print(fecha_completa)
print(fecha_completa.day)
print(fecha_completa.year)

fecha_personalizada = fecha_completa.strftime('%d/%m/%Y, %H:%M:%S')

print('Mi fecha: ',fecha_personalizada) """
#-----------------------------------#
""" import math

print('raiz cuadrada de 10: ',math.sqrt(10))
print('numero pi: ',math.pi)
print('redondear: ',math.ceil(6.24984545))
print('redondear: ',math.floor(6.24984545)) """
#-----------------------------------#
import random

print('numero aleatorio: ',random.randint(15,67))