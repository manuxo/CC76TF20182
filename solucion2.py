"""
Solucion 2
Pablo Galarza
"""


import math
import heapq as hq
import random
from Leer import leerDataSet,leerArchivo
   

def prim(G):
    n = len(G)
    arista = []
    costo = [math.inf]*n
    costo[0] = 0
    parents = [-1]*n
    visitados = [False]*n
    hq.heappush(arista,(0,0))
    
    while len(arista)>0 :
        _,u = hq.heappop(arista)
        if not visitados[u]:
            visitados[u] = True
            for v,w in G[u]:
                if not visitados[v] and w < costo[v]:
                    costo[v] = w
                    parents[v] = u
                    hq.heappush(arista,(w,v))
                    
    return parents,costo
           

def crearG(centrosPoblados):
    
    n = len(centrosPoblados)
    Gp = [[] for x in range(n)]
    for u in range(n):
        v = random.randint(0,n-1)
        while u != v:
            distancia = pow(pow(centrosPoblados[u].coordX-centrosPoblados[v].coordX,2)+pow(centrosPoblados[u].coordY-centrosPoblados[v].coordY,2),1/2)
            Gp[u].append((v, distancia))
            
    return Gp


if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1,5)
    departamentos = leerArchivo("departamentos.txt")
    G = crearG(centrosPoblados)
    
    parents, costo = prim(G)
    
    
""""
G = [
        [(1,2)],
        [(2,10)],
        [(3,7)],
        [(4,2)],
        [(5,1)],
        [(0,1)]
    ]
"""
    
    print(G)
    print(parents)
    print(costo)
        

    
