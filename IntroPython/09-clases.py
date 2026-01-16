class OperasBas:
    #declaracion con propiedades
    num1=0
    num2=0
    res=0
    #declaracion del constructor this
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
    #declaracion de metosos de clase
    
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es: ".format(self.res))
        
def main():
    obj=OperasBas(4,6)
    obj.suma()

if __name__ == "__main__":
    main()