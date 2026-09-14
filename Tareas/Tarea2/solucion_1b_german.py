"""
Solucion punto 2
"""
#%% Solución Ejericio 1b

import numpy as np
import pandas as pd 
from IPython.display import display

# Posiciones del tablero 
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Lista de diccionarios para crear el dataframe 
lst_dict_1b = []

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
            
            if ((0 <= posicion_l_vecino ) and ( posicion_l_vecino <= 7 )) and ((0 <= posicion_n_vecino ) and ( posicion_n_vecino <= 7 )): 
                
                # Agrego el vecino a la lista de vecinos
                lst_N_x.append(f"{letras[posicion_l_vecino]}{numeros[posicion_n_vecino]}")
                
                # Aumento el cardinal de la lista de vecinos en 1
                cardinal += 1
        
        # Lleno cada uno de las filas de la tabla. En total debería tener una lista de 64 diccionarios
        lst_dict_1b.append({"x": f"{letras[l]}{numeros[n]}", "N(x)": lst_N_x, "|N(x)|": cardinal}) 
        
# Creo la tabla a partir de la lista de diccionarios 
tabla_1b = pd.DataFrame(lst_dict_1b)
        
with pd.option_context("display.max_rows", None):
    display(tabla_1b)
    
# print(tabla_1b.to_string)
        
#%% Solución Ejericio 1c, 1d y 1e

# La matriz de transición será una matriz de diccionarios 
matriz_transicion = []

# Construcción de la matriz de transición 
## p1: Son los estados de partida. Son las filas de la matriz de transición
## p2: Son los estados de llegada. Son las columnas de la matriz de transición

for p1 in range(len(lst_dict_1b)): 
    
    # Creo el diccionario asociado al estado de partida
    dct_p1 = {"x": lst_dict_1b[p1]["x"]}
    
    for p2 in range(len(lst_dict_1b)): 
        
        # Cada una de las columnas son los estados de llegada de la matriz de transición        
        if (lst_dict_1b[p2]["x"] in lst_dict_1b[p1]["N(x)"]):
            dct_p1[lst_dict_1b[p2]["x"]] = 1 / lst_dict_1b[p1]["|N(x)|"]
        else: 
            dct_p1[lst_dict_1b[p2]["x"]] = 0
        
    matriz_transicion.append(dct_p1)
        
# Creo la tabla a partir de la lista de diccionarios 
matriz_transicion_df = pd.DataFrame(matriz_transicion)
        
with pd.option_context("display.max_rows", None):
    display(matriz_transicion_df)
    

                
# %%

def calular_probabilidades_transicion_distintas_cero(posicion):
    # Lista de probabilidades de transición distintas de cero
    lst_prob = []

    for p1 in range(len(matriz_transicion)): 
        
        if (matriz_transicion[p1]["x"] == posicion):
            
            for p2 in matriz_transicion[p1]:
                
                if (p2 != "x") and (matriz_transicion[p1][p2] > 0): 
            
                    # Determinar cuáles son los estados de llegada que tienen probabilidades de transición distintas de 0
                    lst_prob.append((p2, matriz_transicion[p1][p2]))
                    
    print(f"Para {posicion} las probabildades de transición mayores a cero son", lst_prob)    
    
calular_probabilidades_transicion_distintas_cero("h8")
calular_probabilidades_transicion_distintas_cero("g1")
calular_probabilidades_transicion_distintas_cero("b7")
calular_probabilidades_transicion_distintas_cero("f7")
calular_probabilidades_transicion_distintas_cero("e5")

            
            

#%%