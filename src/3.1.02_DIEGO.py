def pedir_numero_asignaturas() -> int:
    error = True
    while error:
        try:
            num = int(input("introduzca asignatura"))
            if not (0 <= num <= 10):
                raise ValueError
        except ValueError:
            print("Error")
        else:
            error = False

    return num


def pedir_asignatura(indice: int) -> str:
    return input(f"{indice}. ")


def crear_asignaturas(num_asignaturas) -> tuple:
    print("Introdzca sus asignaturas: ")
    asignaturas = tuple(pedir_asignatura(i + 1) for i in range (num_asignaturas))

    return asignaturas


def crear_lista_asignaturas():



def mostrar_lista(asignaturas):
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")


def main():
    num_asignaturas = pedir_numero_asignaturas()
    asignaturas = crear_lista_asignaturas(num_asignaturas)

    mostrar_lista(asignaturas)
    print()


if __name__ == "__main__":
    main()