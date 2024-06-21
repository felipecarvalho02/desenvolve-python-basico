# -*- coding: utf-8 -*-
"""mod6lista2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vHsBmvWAaOjjxw7HcSKvBr9oWo7mbKqP
"""

import random

# Construção da lista de valores aleatorios
lista1, lista2 =[], []
for i in range(20):
  lista1.append(random.randint(0, 20))
  lista2.append(random.randint(0, 20))

print(sorted(lista1))
print(sorted(lista2))

inters = []
  #caminhar em uma lista, verificar
  #a participação de cada elemento na segunda lista
for elemento in lista1:
 if elemento in lista2 and elemento not in inters:
  inters.append(elemento)

inters.sort()
for i in inters:
  print(f"{i}:  ({lista1.count(i)}, {lista2.count(i)})")