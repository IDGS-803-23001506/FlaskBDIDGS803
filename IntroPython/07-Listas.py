'''
Una lista es una secuencia de elementos
se crea con []
'''

lista1=["Diario", 33, 9.5, True, "German", 20.8]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Pedro")
print(lista1)

lista1.insert(2,"Ana")
print(lista1)

lista1.extend(["uno", 1.1, "False"])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop()
print(lista1)

lista2=["tres","cuatro"]
lista3=lista1+lista2
print(lista3)

print(lista2*4)
lista4=[2,1,5,4,3]
lista4.sort()
print(lista4)