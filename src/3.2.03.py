"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

def main():
    diccionario_frutas = {"platano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.7}
    fruta = input("Introduce la fruta que quieres comprar: ").lower()
    kilos = int(input("Introduce los kilos de fruta que quieres comprar: "))
    
    if fruta not in diccionario_frutas:
        print(f"{fruta.capitalize()} no es una fruta que tengamos en venta.")
    else:
        print(f"{kilos} kg de {fruta} cuestan {kilos*diccionario_frutas[fruta]} €.")


if __name__ == "__main__":
    main()