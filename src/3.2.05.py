"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""


def main():
    diccionario_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditos = 0
    for asignatura in diccionario_asignaturas.items():
        print(f"{asignatura[0]} tiene {asignatura[1]} créditos")
        creditos += asignatura[1]
    print(f"El número total de créditos del curso es: {creditos}")

if __name__ == "__main__":
    main()