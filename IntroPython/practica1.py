'''
operacion de multiplicacion de a x b
a=3
b=4

salida: 3+3+3+3=12
'''
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

x = 0
suma = ""

while num2 > 0:
    x += num1
    suma += str(num1)
    if num2 > 1:
        suma += "+"
    num2 -= 1
    
print(suma,"=", x)

