# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:14:09 2023

@author: Ricardo Ismael Gomez Sanchez
"""

def Algoritmo_prim(w, n, s):
# s = vertice inicial
# w = peso
# n = numero de nodos
    v = []
    while(len(v) != n):
        v.append(0) # Lista de marcadores para nodos visitados (0 = no visitado, 1 = visitado)
    v[s] = 1 # Marcar el nodo inicial como visitado
    E = [] # Lista para almacenar los arcos del árbol mínimo
    suma = 0 # Variable para almacenar la suma de los pesos del árbol mínimo
    for i in range(0, n-1):
        minimo = 99999 # Valor inicial alto para encontrar el mínimo
        agregar_v = 0 # Nodo a agregar al árbol mínimo
        e = [] # Arco a agregar al árbol mínimo
        for j in range(0, n):
            if(v[j] == 1): # Si el nodo j está marcado como visitado
                for k in range(0, n):
                    if(v[k] == 0 and w[j][k] < minimo): # Si el nodo k no está marcado como visitado y el peso j->k es menor que el mínimo actual
                        agregar_v = k # Actualizar el nodo a agregar al árbol mínimo
                        e = [j, k] # Actualizar el arco a agregar al árbol mínimo
                        minimo = w[j][k] # Actualizar el mínimo
        
        
        suma += w[e[0]][e[1]] # Sumar el peso del arco al total de la suma
        v[agregar_v] = 1 # Marcar el nodo k como visitado
        E.append(e) # Agregar el arco al árbol mínimo
        print('\nCamino elegido:')
        print(e)
        print('Peso del camino:')
        print((minimo))
        print('Peso actual de ruta:')
        print((suma))
    return [E, suma] # Retornar el árbol mínimo (lista de arcos) y la suma de los pesos

n = 5 # Número de nodos en el grafo
s = 0 # Nodo inicial
inf=9999999
w=[
#nodos A,   B,   C,   D,   E
      [inf, 1,   3,   2,   4  ],  #con nodo A=0
      [1,   inf, 2,   inf, inf],  #con nodo B=1
      [3,   2,   inf, 1,   inf],  #con nodo C=2
      [2  , inf, 1,   inf, 1  ],  #con nodo D=3
      [4,   inf, inf, 1  , inf],  #con nodo E=4
      ]####-####-####-####-####-####-####-

#NOTA: El vertice 1 = vertice 0...
resultado = Algoritmo_prim(w, n, s) # Llamar a la función de algoritmo de Prim
print("El árbol es: ")
print(resultado[0]) # Imprimir los arcos del árbol mínimo
print("El peso de la gráfica es: ")
print(resultado[1]) # Imprimir la suma de los pesos del árbol mínimo
