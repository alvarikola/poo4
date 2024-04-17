class EjemploExecpciones:
    # ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int):
        if (den == 0):
            raise ZeroDivisionError("No puedes dividir por 0")


    # ValueError
    def valueError(numero):
        if numero + int("x"):
            raise ValueError("No puedes sumar una letra")


    # FileNotFoundError
    def fileNotFoundError():
        pass


    # TypeError
    def typeError(a:int, b:str):
        if a + b:
            raise TypeError("No puedes sumar a un string")


    # PermissionError

    # IndexError

    # KeyboardInterrupt

    # UnicodeDecodeError

    # AttributeError