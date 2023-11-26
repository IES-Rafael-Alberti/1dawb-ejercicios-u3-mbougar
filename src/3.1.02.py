def introducirAsignatura() -> str:
    """Pide un valor asignatura.

    Returns:
        asignatura: string introducida por el usuario.
    """
    loop = False
    while not loop:
        print("Introduzca una asignatura: ", end="")
        try:
            asignatura = input()
        except Exception:
            print("Error introduciendo la asignatura, vuelva a intentarlo: ", end="")
        else:
            loop = True
    return asignatura


def introducirOpcion() -> str:
    """Pide un valor opcion.

    Returns:
        opcion: string introducida por el usuario.
    """
    loop = False
    while not loop:
        try:
            opcion = input()
            if opcion == "s" or opcion == "n":
                return opcion
            else:
                raise Exception
        except Exception:
            print("Error introduciendo la opcion, vuelva a intentarlo: ", end="")


def main():
    listaAsignaturas = []
    loop = False
    while not loop:
        print("¿Quiere introducir una asignatura? s/n: ", end="")
        opcion = introducirOpcion()
        if opcion == "s": 
            asignatura = introducirAsignatura()
            listaAsignaturas.append(asignatura)
        else:
            loop = True
    for i in range(0, len(listaAsignaturas)):
        print(f"Yo estudio {listaAsignaturas[i]}")


if __name__ == "__main__":
    main()