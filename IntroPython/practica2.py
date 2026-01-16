'''
realizar un programa que nos permita realizar las operaciones basicas
+,-,*,/ utilizando una funcioncion para cada funcion y pedir  los dos parametros, lo primero que se visualizara sera el menu
1.-Suma
2.-Resta
3.-Multiplicar
4.-Dividir
5.-Salir
Opcion:
Luego de realizar la operacion se debe mostar el resultado y regresar al menu
'''
import os


def sumar(num1,num2):
    suma=num1+num2
    return suma

def restar(num1,num2):
    resta=num1-num2
    return resta

def multiplicar(num1,num2):
    mult=num1*num2
    return mult

def dividir(num1,num2):
    div=num1/num2
    return div

def main():
    opcion=0
    while opcion!=5:
        print("1.-Suma")
        print("2.-Resta")
        print("3.-Multiplicar")
        print("4.-Dividir")
        print("5.-Salir")
        opcion=int(input("Seleccione una opcion: "))
        
        if opcion==5:
            print(os.system("cls"))
            break;
        
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
        
        if num2 == 0 and opcion == 4:
            print("No se puede dividir entre cero")
            main()
        
        if opcion==1:
            print("La suma es: ", sumar(num1, num2))
        elif opcion==2:
            print("La resta es: ", restar(num1, num2))
        elif opcion==3:
            print("La multiplicacion es: ", multiplicar(num1, num2))
        elif opcion==4:
            print("La division es: ", dividir(num1, num2))



if __name__ =="__main__":
    print("Ejecutando el modulo 05-funciones.py")
    main()