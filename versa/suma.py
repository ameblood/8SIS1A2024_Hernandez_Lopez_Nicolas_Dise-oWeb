while True:
    menu = """
    Menú
    1- SUMA
    2- RESTA
    3- SALIR
    """
    print(menu)
    op = int(input("Introduzca una opción: "))

    if op == 1:
        n1 = float(input("Dame un número entero: "))
        n2 = float(input("Dame otro número entero: "))
        n3 = n1 + n2
        print("El resultado de la suma es", n3)
    elif op == 2:
        n1 = float(input("Dame un número entero: "))
        n2 = float(input("Dame otro número entero: "))
        n3 = n1 - n2
        print("El resultado de la resta es", n3)
    elif op == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
