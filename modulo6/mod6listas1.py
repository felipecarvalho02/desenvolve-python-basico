# -*- coding: utf-8 -*-
"""mod6listas1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17YVAFLZAUb4D0DEf6klbdNgnT3HwPfsT
"""

aleatorios.index(-76)

"""#Exercicio lista
Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100. Em seguida imprima na ordem estabeleciada:


*   A lista ordenada, sem modificar a lista original
*   A lista original
*   O indice do mairo valor da lista
*   O indice do menor valor da lista



"""

import random

# Construção da lista de valores aleatorios
aleatorios = []
for i in range(20):
  valor = random.randint(-100, 100)
  aleatorios.append(valor)

  ### aleatorios.sort() modifica a lista original
  print(sorted(aleatorios))
  print(aleatorios)
  print("O maior valor esta no indice:  ",
        aleatorios.index(max(aleatorios)) )

  print("O menor valor esta no indice:  ",
        aleatorios.index(min(aleatorios)))