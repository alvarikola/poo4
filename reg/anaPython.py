import re

class AnaPython:
    @staticmethod
    def countDef(codigo:str) -> int:
        patron = "^def.+:$"
        result = re.findall(patron, codigo) 
        contador = 0
        for i in range(len(result)):
            contador += 1
            print(i)
        return contador
    



if __name__ == "__main__":
    codigo = """
def egsg():
    pass
    
def aefga()
    pass
    
efref:
    pass
"""
    print(AnaPython.countDef(codigo))