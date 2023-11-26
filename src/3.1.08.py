""" 
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""


def comprobar_palindromo(palabra):
    contador1 = 0
    contador2 = -1
    palindromo = True
    while contador1 < len(palabra) / 2:
        if palabra [contador1] != palabra [contador2]: 
            palindromo = False
            return palindromo

        contador1 += 1
        contador2 -= 1
    
    return palindromo


def main():

    palabra = input("Introduzca una palabra: ")
    palabra = list(palabra)
    if comprobar_palindromo(palabra) == True:
        print(f"{palabra} es un palindromo")
    else:
        print(f"{palabra} no es un palindromo")    
        
                    
if __name__ == "__main__":
    main()

