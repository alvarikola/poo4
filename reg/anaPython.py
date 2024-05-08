import re

class AnaPython:
    @staticmethod
    def countDef(codigo:str) -> int:
        patron = "def\s+\w+\(\):"
        result = re.findall(patron, codigo)
        return f"Se han encontrado {len(result)} funciones"

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