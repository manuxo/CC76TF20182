"""
Solucion 2
Pablo Galarza
"""

import heapq as hq
import random
import math
from calcularDistancia import calcularDistancia
from Leer import leerDataSet
   
def prim(G,centrosPoblados,inicio = 0):
    #lista de aristas
    resultado = []

    dist = {}
    for cep in centrosPoblados:
        dist[cep.codigo] = math.inf
    padres = {}
    for cep in centrosPoblados:
        padres[cep.codigo] = ''
    visitados = {}
    for cep in centrosPoblados:
        visitados[cep.codigo] = False
    q = []
    hq.heappush(q, (0,centrosPoblados[inicio].codigo))
    while len(q) > 0:
        _,u = hq.heappop(q)
        if not visitados[u]:
            visitados[u] = True
            for w,v in G[u]:
                if not visitados[v] and w < dist[v]:
                    dist[v] = w
                    padres[v] = u
                    resultado.append((u,v))
                    hq.heappush(q, (w,v))
    return padres,dist,resultado


#retorna diccionario
def generarGrafo(centrosPoblados):
    grafo = {}
    for cep in centrosPoblados:
        grafo[cep.codigo] = []
    for cep in centrosPoblados:
        copia = centrosPoblados[:] # genera una copia de todos los centros poblados
        copia.remove(cep) #removemos el cep seleccionado para no generar un camino al mismo punto
        destinosPorCep = random.randint(3,5) # seleccionamos entre 3 y 5 destinos por cada centro poblado
        for _ in range(destinosPorCep):
            destino = random.choice(copia) #seleccionamos un destino al azar
            copia.remove(destino) #removemos el destino para que no se repita
            #Generamos una nueva arista
            distancia = calcularDistancia(cep,destino)
            arista = (distancia,destino.codigo)
            grafo[cep.codigo].append(arista)
    return grafo

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    centrosPoblados = leerDataSet("dataset.csv",1)
    tipoMuestra = {
        'RESTANTES':0,
        'DEPARTAMENTALES':1,
        'PROVINCIALES':2,
        'DISTRITALES':3
    }
    muestra = []
    for cep in centrosPoblados:
        if cep.capital == tipoMuestra['DEPARTAMENTALES']:
            muestra.append(cep)
    grafo = generarGrafo(muestra)
    padres,distancias,resultado = prim(grafo,muestra)
    print(resultado)

    #Config mapa
    plt.figure(figsize=(15,5))
    plt.title("Mapa")
    plt.xlabel("Coord X")
    plt.ylabel("Coord Y")
    #Pintando mapa
    x = []
    y = []
    for cep in centrosPoblados:
        x.append(cep.coordX)
        y.append(cep.coordY)
    plt.plot(x,y,'ro')

    def buscarCentroPoblado(codigo):
        for cep in centrosPoblados:
            if cep.codigo == codigo:
                return cep

    def pintarGrafo(grafo,color):
        for codigo in grafo:
            origen = buscarCentroPoblado(codigo)
            for arista in grafo[codigo]:
                _,d = arista
                destino = buscarCentroPoblado(d)
                x = [origen.coordX,destino.coordX]
                y = [origen.coordY,destino.coordY]
                plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")
    def pintarAristas(aristas,color):
        for arista in aristas:
            origen,destino = arista
            o = buscarCentroPoblado(origen)
            d = buscarCentroPoblado(destino)
            x = [o.coordX,d.coordX]
            y = [o.coordY,d.coordY]
            plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")

    #Pintamos el grafo inicial
    pintarGrafo(grafo,"blue")
    #Pintamos el arbol de expansion minima generado con Prim
    pintarAristas(resultado,"white")
    plt.show()