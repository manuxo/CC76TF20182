"""
Luis Angel
"""
import math
import random
from Leer import leerDataSet, leerArchivo

def floydWarshall(G):
    tamano = len(G)
    maCostos = [[math.inf]*tamano for _ in range(tamano)]
    maPadres = [[-1]*tamano for _ in range(tamano)]
    for nodo in range(tamano):
        maCostos[nodo][nodo] = 0
        for vecino, peso in G[nodo]:
            maCostos[nodo][vecino] = peso
            maPadres[nodo][vecino] = nodo
            
    for k in range(tamano):
        for i in range(tamano):
            for j in range(tamano):
                pesoAcumulado = maCostos[i][k] + maCostos[k][j]
                if maCostos[i][j] > pesoAcumulado:
                    maCostos[i][j] = pesoAcumulado
                    maPadres[i][j] = k
                    
    return maPadres


def crearG(centrosPoblados):
    n=len(centrosPoblados)
    
    uCodigos=[]
    for u in range(n):
        uCodigos.append((u,centrosPoblados[u].codigo))
    
    G=[[] for x in range(n)]
    for u in range(n):
        v=random.randint(0,n-1)
        peso=pow(pow(centrosPoblados[u].coordX-centrosPoblados[v].coordX,2)+pow(centrosPoblados[u].coordY-centrosPoblados[v].coordY,2),1/2)
        G[u].append((v, peso))
        """
        if u!=u-1:
            d[u]=pow(pow(centrosPoblados[u].coordX-centrosPoblados[u+1].coordX,2)+pow(centrosPoblados[u].coordY-centrosPoblados[u+1].coordY,2),1/2)
        else:
            d[u]=0
            """   
    return G, uCodigos
    


"""def crearG(centrosPoblados):
    n=len(centrosPoblados)
    G=[[] for x in range(n)]
    
    distancias=distancia(centrosPoblados)
    
    uCodigos=[]
    for u in range(n):
        uCodigos.append((u,centrosPoblados[u].codigo))
    
    for u in range(n):
        G[u].append((u,distancias[u]))
            
    
    return G"""





if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1,5)
    departamentos = leerArchivo("departamentos.txt")
    G, uCodigos =crearG(centrosPoblados)
    """
    G = [
        [(1,2)],
        [(2,10)],
        [(3,7)],
        [(4,2)],
        [(5,1)],
        [(0,1)]
    ]
    """
    
    
    
    matrizPadres=floydWarshall(G)
    print(G)
    print(matrizPadres)
    
  
    #print(crearG(centrosPoblados))

    
    