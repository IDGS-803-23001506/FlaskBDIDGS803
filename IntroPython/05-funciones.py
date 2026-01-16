import os


def function1():
    os.system("cls")
    print("IDGS803 - Desarrollo web profesional")

def function2(nombre):
    print("Hola ", nombre)
    
def function3(num1,num2):
    suma=num1+num2
    return suma

def main():
    funcion1()
    funcion2("Juan Perez")
    resultado=funcion3(2,3)
    print("el resultado de la suma es: ", resultado)
    

if __name__ =="__main__":
    print("Ejecutando el modulo 05-funciones.py")
    main()