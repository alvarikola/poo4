import re
class RegExample:
    def __init__(self) -> None:
        pass


    @staticmethod
    def buscar(texto:str):
        # El patron de palabras que empiecen con vocal minúscula
        patron = "\\b[seiou][^\\s.,]*"
        result = re.findall(patron, texto)
        return result
    

    @staticmethod
    def validURL(url:str) -> bool:
        patron = "^https?://([a-z0-9].+)+\..+"
        result = re.search(patron, url)
        if result == None:
            return False
        else:
            return True





    
