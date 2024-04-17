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
    def fileNotFoundError():
        pass #esto es con open


    # TypeError
    def typeError(self, a:int, b:str):
        if type(a) == str:
            raise TypeError("No es el tipo correcto")
        
        return type(a)


    # PermissionError
    def permissionError(self):
        pass
    # IndexError
    def indexError(self):
        pass
    # KeyboardInterrupt
    def keyboardInterrupt(self):
        pass
    # UnicodeDecodeError
    def unicodeDecodeError(self):
        pass
    # AttributeError
    def attributeError(self):
        pass