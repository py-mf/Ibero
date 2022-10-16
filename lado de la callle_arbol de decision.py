# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:25:40 2022

@author: yanpa
"""
#Base de datos de entrenamiento

calle = {"A": [60, 10, 3],
        "B": [20, 100, 2],
        "C": [70, 70, 4],
        "D": [40, 20, 1]   
        }

for key in calle.values():
    if key[0] > 50:
        if key[1] > 50:
            print("Lado 4")
        else: 
            print("Lado 3")
    else:
        if key[1] > 50:
            print("Lado 2")
        else:
            print("lado 1")
            
        
#Base de datos de prueba

calle_2 = {"X": [100, 25],
           "Y": [50, 50]
    }

for key in calle_2.values():
    if key[0] > 50:
        if key[1] > 50:
            print("Lado 4")
        else: 
            print("Lado 3")
    else:
        if key[1] > 50:
            print("Lado 2")
        else:
            print("lado 1")