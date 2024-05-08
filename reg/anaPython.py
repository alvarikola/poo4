import re

class AnaPython:
    @staticmethod
    def countDef(codigo:str) -> int:
        patron = "def\s+\w+\(\):"
        result = re.findall(patron, codigo)
        return f"Se han encontrado {len(result)} funciones"
    

    def encontrarVariable(codigo:str) ->list:
        patron = "[a-zA-Z]+\s*=\s*\w+"
        result = re.findall(patron, codigo)
        return result

if __name__ == "__main__":
    codigo = """
def egsg():
    hola=1
    
def aefga()
    pass
    
efref:
    pass
    
adios = 1
"""
    print(AnaPython.countDef(codigo))
    print(AnaPython.encontrarVariable(codigo))
