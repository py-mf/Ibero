# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:02:27 2022

@author: yanpa
"""

'''CIENCIA DE DATOS'''

from tkinter import * 

class CienciaDatos():
    def __init__(self):
        self.administracion = " "
        self.estadistica = " "
        self.informatica = " "
        
    def recolectar(self):
        print()
        print("¡Hola! ¡Sea bienvenido!")
        print()
        self.administracion = input("¿Conoces el concepto de administración? \n ¿Sí o no?: ").upper()
        print()
        self.estadistica = input("¿Conoces el concepto de estadística? \n ¿Sí o no?: ").upper()
        print()
        self.informatica = input("¿Conoces el concepto de informática? \n ¿Sí o no?: ").upper()
        print()
        
    def procesar(self):
        if self.administracion or self.estadistica or self.informatica == "SÍ":
            print("¡Perfecto!")
            print()
            
        if self.administracion == "NO":
            print("La administración es la disciplina científica que tiene por objeto de estudio las organizaciones constituyendo una sociotecnología6​ encargada de la planificación, organización, dirección y control de los recursos (humanos, financieros, materiales, tecnológicos, del conocimiento, etcétera) de una organización, con el fin de obtener el máximo beneficio posible; este beneficio puede ser social o económico, dependiendo de los fines perseguidos por la organización. (WIKIPEDIA, 2022)")
            print()
        if self.estadistica == "NO":
            print("La estadística es una ciencia que estudia la variabilidad, colección, organización, análisis, interpretación, y presentación de los datos, así como el proceso aleatorio que los genera siguiendo las leyes de la probabilidad. (WIKIPEDIA, 2022)")
            print()
        if self.informatica == "NO":
            print("La ciencia de la información es un campo académico que se ocupa principalmente del análisis, la recopilación, la clasificación, la manipulación, el almacenamiento, la recuperación, el movimiento, la difusión y la protección de la información. (WIKIPEDIA, 2022)")
            print() 
            
    def presentar(self):
        print("La ciencia de datos es un campo interdisciplinario que, con métodos científicos, extrae conocimiento de datos estructurados o no estructurados​. Es una combinación de campos de análisis de datos como la estadística, la minería de datos, el aprendizaje automático, y la analítica predictiva. El concepto ciencia de datos reúne estadísticas, análisis de datos, aprendizaje automático, y sus métodos relacionados, para comprender y analizar los fenómenos reales​. Emplea técnicas y teorías extraídas de muchos campos dentro del contexto de las matemáticas, la estadística, la ciencia de la información, y la informática. (WIKIPEDIA, 2022)")
        print()
        print("¡Gracias por participar!")
        
datascience = CienciaDatos()
a = datascience.recolectar()
b = datascience.procesar()
c = datascience.presentar()

print(a)
print(b)
print(c)

janela = Tk()
janela.title("CIENCIA DE DATOS")
texto = Label(janela, text="¡Sea bienvenido! Responda las siguientes preguntas para comenzar.")
texto.grid(column=0, row=0, padx=5, pady=5)

aa="La administración es la disciplina científica que tiene por objeto de estudio las organizaciones constituyendo una sociotecnología6​ encargada de la planificación, organización, dirección y control de los recursos (humanos, financieros, materiales, tecnológicos, del conocimiento, etcétera) de una organización, con el fin de obtener el máximo beneficio posible; este beneficio puede ser social o económico, dependiendo de los fines perseguidos por la organización. (WIKIPEDIA, 2022)"

botao = Button(janela, text="Administración", command=c)
botao.grid(column=0, row=1, padx=5, pady=5)

botao2 = Button(janela, text="Estadistica", command=b)
botao2.grid(column=0, row=3, padx=5, pady=5)

botao3 = Button(janela, text="Informatica", command=b)
botao3.grid(column=0, row=5, padx=5, pady=5)

botao4 = Button(janela, text="Ciencia de Datos", command=b)
botao4.grid(column=0, row=7, padx=5, pady=5)

texto_resposta = Label(janela, text="La administración es la disciplina científica que tiene por objeto de estudio las organizaciones constituyendo una sociotecnología6​ encargada de la planificación, organización, dirección y control de los recursos (humanos, financieros, materiales, tecnológicos, del conocimiento, etcétera) de una organización, con el fin de obtener el máximo beneficio posible; este beneficio puede ser social o económico, dependiendo de los fines perseguidos por la organización. (WIKIPEDIA, 2022)")
texto_resposta.grid(column=0, row=2, padx=5, pady=5)

texto_resposta2 = Label(janela, text="La estadística es una ciencia que estudia la variabilidad, colección, organización, análisis, interpretación, y presentación de los datos, así como el proceso aleatorio que los genera siguiendo las leyes de la probabilidad. (WIKIPEDIA, 2022)")
texto_resposta2.grid(column=0, row=4, padx=5, pady=5)

texto_resposta3 = Label(janela, text="La ciencia de la información es un campo académico que se ocupa principalmente del análisis, la recopilación, la clasificación, la manipulación, el almacenamiento, la recuperación, el movimiento, la difusión y la protección de la información. (WIKIPEDIA, 2022)")
texto_resposta3.grid(column=0, row=6, padx=5, pady=5)

texto_resposta4 = Label(janela, text="La ciencia de datos es un campo interdisciplinario que, con métodos científicos, extrae conocimiento de datos estructurados o no estructurados​. Es una combinación de campos de análisis de datos como la estadística, la minería de datos, el aprendizaje automático, y la analítica predictiva. El concepto ciencia de datos reúne estadísticas, análisis de datos, aprendizaje automático, y sus métodos relacionados, para comprender y analizar los fenómenos reales​. Emplea técnicas y teorías extraídas de muchos campos dentro del contexto de las matemáticas, la estadística, la ciencia de la información, y la informática. (WIKIPEDIA, 2022)")
texto_resposta4.grid(column=0, row=8, padx=5, pady=5)


janela.mainloop()