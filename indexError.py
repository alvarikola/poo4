def lista(posicion:int)->int:
    listaFruta = ["Manzana", "Plátano", "Pera"]
    try:
        return listaFruta[posicion]
    except IndexError:
        print("IndexError Realizamos tareas de control de cierre")
    except Exception:
        print("Otro error")


if __name__ == "__main__":
    def main():
        print(lista(4))


    main()
