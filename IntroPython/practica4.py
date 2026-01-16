'''
Pedir al usuario 20 numeros repetidos y sin repetir los almacene en una lista y luego los muestre la lista ordenada de menor a mayor,
tambien nos diga cuantos son repetidos y cuantas veces se repitieron separarlos entre pares e impares

[5.3,2,8,5,3,2,1,4,7,9,6,5,3,2,1,0,4,6,8,9]

5-2
2-3
3-3

pares: [2,8,4,6]
imapres: [5,3,1,7,9]
'''
num=0
lista1=[]
for i in range(20):
    num=int(input("ingresa un numero: "))
    lista1.append(num)
lista1.sort()
listaRepetidos = lista1
print(lista1)

lista1.sort()
listaRepetidos = lista1

for i in range(20):
    contador = 1

    if i == 0 or listaRepetidos[i] != listaRepetidos[i - 1]:
        for j in range(i + 1, len(listaRepetidos)):
            if listaRepetidos[i] == listaRepetidos[j]:
                contador += 1

        if contador > 1:
            print(listaRepetidos[i], "-", contador)

lista4=[]
lista5=[]

for i in range(20):
    if  lista1[i] % 2 == 0:
        lista4.append(lista1[i])
    else:
        lista5.append(lista1[i])
        
        
print("pares: ", lista4)
print("impares: ",lista5)

