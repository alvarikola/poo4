class EjemploExecpciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int):
        if (den == 0):
            raise ZeroDivisionError("No puedes dividir por 0")
        
        return num / den


    # ValueError
    def valueError(self, numero:int, x:str):
        if numero + int(x):
            raise ValueError("No puedes sumar una letra")

        return numero + x

    # FileNotFoundError
    def fileNotFoundError(self, file):
        a = open(file, "r")        #esto es con open
        if a != open:
            raise FileNotFoundError("No se encuentra")
        
        return a
    

    # TypeError
    def typeError(self, a:int, b:str):
        if type(a) == str:
            raise TypeError("No es el tipo correcto")
        
        return type(a)


    # PermissionError
    def permissionError(self):
        a = open("C:\Users/esbirro", "r")
        if a != open:
            raise PermissionError("No tienes permisos")
        
        return a


    # IndexError
    def indexError(self, i:int):
        listaFruta = ["Manzana", "Plátano", "Pera"]
        if i >= len(listaFruta):
            raise IndexError("No esta esa posicion")
        
        return listaFruta[i]
    

    # KeyboardInterrupt
    def keyboardInterrupt(self):
        pass
    # UnicodeDecodeError
    def unicodeDecodeError(self):
        pass
    # AttributeError
    def attributeError(self):
        pass