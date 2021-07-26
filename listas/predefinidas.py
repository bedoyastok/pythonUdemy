cantante = ['hola', 'como', 'estas', 'tu']
numeros = [5, 9, 3, 7, 1, 2]

print(numeros)
numeros.sort()#ordenar
print(numeros)

cantante.append('que bien')#agrgar elemento
cantante.insert(1,'chao')#agregar elemento con indice
print(cantante)

cantante.pop(4)#eliminar dato con indice
print(cantante)

cantante.remove('hola')#eliminar elemento por su nombre
print(cantante)

print(numeros)
numeros.reverse()#invertir la lista
print(numeros)

print('estas' in cantante)#buscar dato en lista

print(len(cantante))#contar numero de elementos

print(numeros.count(5))#cuantes veces aparece un elemnto en la lista

print(cantante.index('que bien'))#obtener indice

cantante.extend(numeros)#unir dos listas
print(cantante)


