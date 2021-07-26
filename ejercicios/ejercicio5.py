num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa otro numero: "))
entre = 0

if num1 < num2:
    for entre in range(num1,num2+1):
        print(entre)
else:
    for entre in range(num2,num1+1):
        print(entre)