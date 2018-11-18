"""
    Manuel
"""
import heapq as hq
from Leer import leerDataSet,leerArchivo
from unionfind import union,find

def kruskal(G,id):
    aristas = []
    resultado = []
    for arista in G:
        costo,nodo,vecino = arista
        hq.heappush(aristas,(costo,nodo,vecino))

    while len(aristas):
        _,u,v = hq.heappop(aristas)
        pu = find(id,u)
        pv = find(id,v)
        if pu != pv:
            resultado.append((u,v))
            union(id,pu,pv)
    return resultado

if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1,5)
    departamentos = leerArchivo("departamentos.txt")
    id = {}
    for cep in centrosPoblados:
        id[cep.codigo] = cep.codigo

    G = [
        (2,'683891','683892'),
        (10,'683891','683893'),
        (7,'683892','683895'),
        (2,'683893','683895'),
        (1,'683893','683894'),
        (1,'683895','683894')
    ]
    arbolExpMin = kruskal(G,id)
    print(arbolExpMin)