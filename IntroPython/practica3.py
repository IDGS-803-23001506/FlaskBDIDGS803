'''
pedir un numero al usuario
mostrar la tabla de multiplica del numero
'''
num1=int(input("ingresa un numero: "))
mul=0

for i in range(10):
    mul=num1*i
    print(num1, "X",  i, "=",mul)
    mul=0