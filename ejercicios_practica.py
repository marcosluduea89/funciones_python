#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Marcos_Ludueña"
__email__ = "marcosluduea89@gmail.com"
__version__ = "1.2"

import random


def imprimir_nombre(nombre, apellido):
    print("El nombre y apellido es el siguiente:")
    print(nombre, apellido,"\n")
    
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)


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


def ej1():
    print('Mi primera funcion')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Marcos','Ludueña')

    # Reemplazar por su nombre y apellido los textos


def ej2():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado

    '''
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    # promedio_re
    promedio_re = promedio(numeros)
    print(promedio_re,"\n")
    # Luego imprimir en pantalla el valor resultante, tal que:
    

def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''

    # Luego de crear la función invocarla en este lugar:
    # lista_ordenada = ordenar(numeros)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar
    lista_ordenada = ordenar(numeros)
    print(lista_ordenada,"\n")


def ej4():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''

    # Invocar lista_aleatoria
    # mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    # print(mi_lista_aleatorio)
    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    print ("La lista random es la siguiente:")
    print(mi_lista_aleatorio,"\n")


def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    inicio = 1
    fin = 9
    numero_a_consultar = 3

    lista_numeros = lista_aleatoria(inicio,fin,cantidad_numeros)
    print("Lista de numeros:")
    print(lista_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    cantidad_tres = contar(lista_numeros, 3)
    print("Numero de veces que se repite {}: ".format(numero_a_consultar))
    print(cantidad_tres)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()



 


 