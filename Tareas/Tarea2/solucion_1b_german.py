"""
Solucion punto 2
"""

import numpy as np
import pandas as pd 
from IPython.display import display

# Posiciones del tablero 
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Lista de diccionarios para crear el dataframe 
lst_dict = []

# Lista de instrucciones 
# Cada instrucción será codificada como una tupla de enteros: 
# Instrucciones: 
## 1. (-2, 1)
## 2. (-1, 2)
## 3. (1, 2)
## 4. (2, 1)
## 5. (-2, -1)
## 6. (-1, -2)
## 7. (1, -2)
## 8. (2, -1)

lst_inst = [(-2, 1), (-1, 2), (1, 2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

# Doble for que recorre el Tablero de Ajedrez

# Nota: Cada pareja l y n me permite identificar una posición en el tablero de ajedrez
for l in range(len(letras)):
    for n in range(len(numeros)): 
        # Cuenta el tamaño de vecinos
        cardinal = 0
        # Lista de vecinos 
        lst_N_x = []
        
        # Itero por cada una de las instrucciones posibles para saber si la instrucción es válida o no lo es
        for pareja in lst_inst: 
            # pareja es un "tuple"
            
            posicion_l_vecino = l + pareja[0]
            posicion_n_vecino = n + pareja[1]
            
            if ((0 < posicion_l_vecino ) and ( posicion_l_vecino < 7 )) and ((0 < posicion_n_vecino ) and ( posicion_n_vecino < 7 )): 
                
                # Agrego el vecino a la lista de vecinos
                lst_N_x.append(f"{letras[posicion_l_vecino]}{numeros[posicion_n_vecino]}")
                
                # Aumento el cardinal de la lista de vecinos en 1
                cardinal += 1
        
        # Lleno cada uno de las filas de la tabla. En total debería tener una lista de 64 diccionarios
        lst_dict.append({"x": f"{letras[l]}{numeros[n]}", "N(x)": lst_N_x, "|N(x)|": cardinal}) 
        
# Creo la tabla a partir de la lista de diccionarios 
tabla_1b = pd.DataFrame(lst_dict)
        
with pd.option_context("display.max_rows", None):
    display(tabla_1b)
    
# print(tabla_1b.to_string)
        

                
        