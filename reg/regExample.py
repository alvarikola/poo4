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
        patron = "^https://.+/$"



if __name__ == "__main__":
    text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ex imperdiet, bibendum ante dapibus, feugiat mauris. Vestibulum sed leo felis. In dapibus pellentesque risus et efficitur. Praesent ante metus, dictum non hendrerit egestas, tempus ornare ex. Vivamus lorem massa, consequat ac malesuada ut, accumsan pretium velit. In consectetur, eros sed consequat blandit, justo ipsum eleifend enim, eget bibendum metus elit in eros. Phasellus euismod, dui ut ullamcorper cursus, velit lorem blandit ex, a auctor turpis sem at dolor. Nam aliquet cursus leo eget ullamcorper. Mauris nunc nisl, fermentum eu viverra eget, tempor a mi. Suspendisse potenti. Donec mollis accumsan risus vel ornare.

Aliquam lacinia orci ac consectetur sagittis. In vulputate, lorem non facilisis malesuada, lacus nisl volutpat sapien, quis ullamcorper urna felis at elit. Pellentesque sodales nunc risus, in convallis nisi dignissim id. Morbi interdum arcu velit. Donec sodales feugiat purus, at ultricies mauris scelerisque sit amet. Etiam eget ex mauris. Donec rhoncus fringilla tincidunt.

Proin nec lectus sed metus bibendum aliquet. Phasellus varius nunc in orci convallis, ut consectetur erat tempor. Duis tincidunt mauris pretium, eleifend massa quis, dapibus quam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris tristique a mauris id malesuada. Vestibulum eros tellus, interdum vel efficitur sit amet, tempus sed ipsum. Quisque ante erat, interdum vel ligula quis, auctor consequat elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In auctor dapibus massa, varius tempus eros suscipit sed. Nunc placerat, sapien varius ultricies semper, lacus erat auctor lectus, sollicitudin gravida dolor felis eu metus.

Cras semper porta ante in semper. Fusce lectus dolor, maximus ut vulputate sed, condimentum vitae lacus. Integer sit amet mauris sit amet orci posuere iaculis. Proin in nulla metus. Morbi at semper magna. Nulla ultrices hendrerit efficitur. Ut id sodales massa. Nulla fermentum hendrerit fringilla. Fusce malesuada eros rutrum massa eleifend consequat. Vivamus faucibus ex quis elit posuere, a efficitur urna pulvinar. Sed molestie commodo elementum.

Nullam eget neque a metus accumsan rutrum sit amet eget nunc. Nulla sodales, tellus vitae laoreet mattis, leo enim sodales libero, et posuere odio urna ac augue. Duis et urna mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse purus leo, interdum et orci at, faucibus volutpat turpis. Maecenas non rutrum nibh, posuere tincidunt quam. In hac habitasse platea dictumst. Sed venenatis pretium quam, interdum posuere neque vestibulum pellentesque. Sed sed porta nulla, ut gravida elit. Donec a nisi consectetur, posuere tellus et, gravida elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed id faucibus neque. Proin quis enim malesuada, mattis leo eu, viverra erat.
"""
    print(MinVoc.buscar(text))
    
