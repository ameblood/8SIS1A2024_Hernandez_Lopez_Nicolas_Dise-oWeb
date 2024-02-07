import os
import random

def main():
    bandera = True
    while bandera:
        try:
            print("Inicia el juego")
            numero_canicas = int(input("Ingresa el número de canicas con las cuales vas a jugar -> "))
            if numero_canicas < 2:
                print("Solo se puede jugar con dos o más canicas")
            else:
                print("Nivel fácil")
                facil(numero_canicas)
            break
        except ValueError:
            print("Ingresa un número válido")

def facil(numero):
    lista = []
    i = 0
    while i < numero:
        try:
            color = input("Ingresa el color de la canica -> ")
            color = color.lower()
            color = color.strip()
            if color.isnumeric():
                print("No puedes ingresar números en los nombres")
            else:
                cantidad = int(input(f"Ingrese el número de canicas de color '{color}': "))
                if i + cantidad > numero:
                    print("La suma de las cantidades no puede superar el número total de canicas.")
                    continue
                lista.extend([color] * cantidad)
                i += cantidad
        except ValueError:
            print("Ingresa valores válidos")

    print("De los colores que elegiste, ingresa el nombre del que quieras y vamos a ver si es el mismo que tengo en mente. Ganarás un punto, pero si pierdes dos veces, ¡game over!")

    ganados = 0
    perdidos = 0
    bandera2 = True

    while bandera2:
        try:
            random.shuffle(lista)
            longitud = len(lista)
            numero_aleatorio = random.randint(0, longitud - 1)
            color_pc = lista[numero_aleatorio]
            print("Colores previamente ingresados:")
            for elementos in lista:
                print("$", elementos)
            color2 = input("Ingresa un color de los que ingresaste: ")
            color2 = color2.lower()
            color2 = color2.strip()
            if color2 == color_pc:
                print("¡Es correcto!")
                ganados += 1
                if ganados == 3:
                    ganador()
                    break
            else:
                print("¡Incorrecto!")
                perdidos += 1
                if perdidos == 3:
                    perdiste()
                    break
        except ValueError:
            print("Error")

def ganador():
    print("¡Ganaste!")

def perdiste():
    print("Pinche perdedor")

main()
