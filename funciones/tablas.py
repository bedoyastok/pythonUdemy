#definir funcion
def tablas(numero):
    print("tabla de multiplicar del numero",numero)
    for cont in range(1,11):
        oper = numero*cont
        print(numero,"x",cont,"=",oper)
    print("\n")



#invocar funcion
numero = int(input("escribe un numero"))
tablas(numero)



#otra forma de usar la funcion
for num in range(1,10):
    tablas(num)