class EjemploExcepciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int):
        if (den == 0):
            raise ZeroDivisionError("No puedes dividir por 0")
        
        return num / den


    # ValueError
    def valueError(self):
        if 1 + int("x"):
            raise ValueError("No puedes sumar una letra")

        return 1 + "x"

    # FileNotFoundError
    def fileNotFoundError(self):
        a = open("hola.txt", "r")
        if a != open:
            raise FileNotFoundError("No se encuentra")
        
        return a
    

    # TypeError
    def typeError(self, a:int):
        if type(a) == str:
            raise TypeError("No es el tipo correcto")
        
        return type(a)


    #PermissionError
    def permissionError(self):
        try:
            a = open("adios.txt", "r")
            a.write("hola")
        except:
            raise PermissionError


    # IndexError
    def indexError(self):
        i = 5
        listaFruta = ["Manzana", "Plátano", "Pera"]
        if i >= len(listaFruta):
            raise IndexError("No esta esa posicion")
        
        return listaFruta[i]
    

    # KeyboardInterrupt
    def keyboardInterrupt(self):
        try:
            prueba = input("Escribe: ")
            if prueba != KeyboardInterrupt:
                True
        except:
            raise KeyboardInterrupt("Se interrumpio el programa")   
        
        
    # UnicodeDecodeError
    def unicodeDecodeError(self):
        try:
            b"\x81".decode("utf-8")
        except UnicodeDecodeError as e:
            raise e
        

    # AttributeError
    def attributeError(self):
        a = "hola".abduzcan
        if a == AttributeError:
            raise AttributeError
        return a
    


