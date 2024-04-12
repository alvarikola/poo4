def lista(posicion:int)->int:
    listaFruta = ["Manzana", "Plátano", "Pera"]
    try:
        return listaFruta[posicion]
    except IndexError:
        return []


if __name__ == "__main__":
    def main():
        print(lista(4))


    main()
