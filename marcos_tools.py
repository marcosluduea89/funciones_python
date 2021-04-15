#!/usr/bin/env python
'''
MarcosTools
---------------------------
Autor: Ludueña Marcos
Version: 1.2
Descripcion:

Módulo con algunas de las funciones que ejemplifican
las herramientas desarrolladas en este curso.
'''

__author__ = "Marcos Ludueña"
__email__ = "marcosluduea89@gmail.com"
__version__ = "1.2"

def promedio(numeros):
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"
    sumatoria_numeros = 0
    cantidad_numeros = 0

    for i in numeros:
        sumatoria_numeros += i
        cantidad_numeros += 1
    promedio = sumatoria_numeros / cantidad_numeros
    print("El promedio es el siguiente:")
    return promedio

def ordenar(numeros):

    for a in range(len(numeros)): # iteracion con un rango de numeros(range) establecido por(tamamaño de la lista) en variable a 
        for b in range(len(numeros)): # idem anterior pero sobre cada indice a ,con una variable b, un total 25 iteraciones
            if numeros[a] > numeros[b]: # para comparar hasta que algun elemento a sea mayor al b y asi ordenar de mayor a menor
                tmp =numeros[a]     # guardamos el mayor numero en variable cualquiera
                numeros[a] = numeros [b] # reemplazo el numero mas grande en la posicion de la ultima iteracion (para comparar)
                numeros[b] = tmp #el mayor numero nuevo ocupa la primera posicion
    print ("La lista ordenada de mayor a menor es la siguiente:")
    return numeros

def lista_aleatoria (inicio, fin, cantidad):

    random_list = []
    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        random_list.append(numero)
    
    return random_list

def contar (lista, num_a_contar):
    contador=0
    for i in range(len(lista)):
        if lista[i] == num_a_contar:
            contador +=1
    return contador

