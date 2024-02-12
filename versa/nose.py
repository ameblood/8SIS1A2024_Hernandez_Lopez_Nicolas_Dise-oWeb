#!/usr/bin/env python
from perceptron import Perceptron

## Datos de hombres y mujeres

input_data = [
    [0, 0, 0, 0, 1],  
    [0, 0, 0, 1, 0],  
    [0, 1, 0, 1, 1],  
    [0, 1, 1, 0, 1], 
    [1, 0, 0, 0, 0],  
    [0, 1, 1, 1, 1],  
    [1, 0, 0, 1, 0],  
    [1, 0, 1, 1, 0]   
]

## Creamos el perceptron

veces=int(input("cuantas veces quieres hacer la prueba?\n"))
veces1 = 1
while veces1 > 0:
    pr = Perceptron(5,0.1) # Perceptron con 3 entradas
    weights = [] # Lista con los pesos
    errors = []  # Lista con los errores
    ## Fase de entrenamiento
    for _ in range(100):
        # Vamos a entrenarlo varias veces sobre los mismos datos
        # para que los 'pesos' converjan
        for person in input_data:
            output = person[-1]
            inp = [1] + person[0:-1] # Agregamos un uno por default
            weights.append(pr._w)
            err = pr.train(inp,output)
            errors.append(err)

    inputs = []
    for i in range(4):
        inputs.append(float(input(f"Ingrese la entrada {i+1} (0 o 1): ")))

    # Predecimos el resultado
    if pr.predict([1] + inputs) == 1: 
        print("El resultado es 1 (True)")
    else: 
        print("El resultado es 0 (False)")
    
    veces -= 1
    veces1 = veces

#print """
#Nota: El resultado puede estar incorrecto. 
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

# ## Fase de graficacion
# import imp

# can_plot = True
# try:
#     imp.find_module('matplotlib')
# except:
#     can_plot = False

# if not can_plot:
#     print ("No es posible graficar los resultados porque no tienes matplotlib")
#     # sys.exit(0)
#     pass

# import matplotlib.pyplot as plt

# plt.plot(errors)
# plt.show()