"""
Luis Angel
"""
import math
import matplotlib.pyplot as plt
from Leer import leerDataSet,leerArchivo
from generarGrafo import generarGrafo
from itertools import groupby

def construirCamino(maPadres, inicio, fin, d):
    inicio,fin = int(inicio), int(fin)
    if(inicio==fin):
        d.append(inicio)
    elif(maPadres[inicio][fin] == -1):
        print("No existe camino")
        return
    else:
        construirCamino(maPadres, inicio, maPadres[inicio][fin], d);
        d.append(fin)
        
    return d

def transformar(uCodigos, buscado):
    n=len(uCodigos)

    nros=[x[0] for x in uCodigos]
    nodos=[x[1] for x in uCodigos]
    for u in range(0, n):
        if nros[u]==buscado:
            return nodos[u]
        else:
            continue
    return -1

    
def creandoArbol(maPadres, uCodigos, inicio, fin):
    resultado=[]
    camino=[]
    construirCamino(maPadres, inicio, fin, camino)
    n=len(camino)
    primerNodo=-1
    for u in range(n):
        nodo=transformar(uCodigos, camino[u])
        if u==0: primerNodo=nodo
        if u+1!=n:
            vecino=transformar(uCodigos, camino[u+1])
            resultado.append((0,str(nodo),str(vecino)))
        else:
            resultado.append((0,str(nodo),str(primerNodo)))
            
    return resultado


def floydWarshall(G, tamano):
    n=len(G)
    maCostos = [[math.inf]*tamano for _ in range(tamano)]
    maPadres = [[-1]*tamano for _ in range(tamano)]
    visitados=[False]*tamano
    dist=[[math.inf]*tamano for _ in range(tamano)]
    for nodos in range(n):
        for distancia, nodo, vecino in G[nodos]:
            maCostos[nodo][nodo] = 0
            maCostos[nodo][vecino] = distancia
            maPadres[nodo][vecino] = nodo
            
    for k in range(tamano):
        for i in range(tamano):
            for j in range(tamano):
                pesoAcumulado = maCostos[i][k] + maCostos[k][j]
                if maCostos[i][j] > pesoAcumulado:
                    maCostos[i][j] = pesoAcumulado
                    maPadres[i][j] = k
    """
    for i in range(tamano):              
        if not visitados[i]:
            visitados[i]=True
            for j in range(tamano):
                if not visitados[j] and maCostos[i][j]<dist[i][j]:
                    maPadres[i][j]=i
    """                
    
           
    return maPadres

def buscar(uCodigos, vecino):
    n=len(uCodigos)

    nros=[x[0] for x in uCodigos]
    nodos=[x[1] for x in uCodigos]
    for u in range(0, n):
        if nodos[u]==vecino:
            return nros[u]
        else:
            continue
    return -1
        
def repetidos(r):
    
    norep = []
    for x in r:
        if x not in norep:
            norep.append(x)
            
    return norep
                
        
def generarGrafoFloyd(muestra):
    G=generarGrafo(muestra)
    n=len(G)
    grafo=[[] for _ in range(n)]
    
    i=0
    r=[]
    for _, nodo, _ in G:
        r.append(int(nodo))
        
    norep=repetidos(r)


    uCodigos=[]
    for nodo in norep:
        uCodigos.append((i, nodo))
        i=i+1

    for u in range(n):
        distancias=[x[0] for x in G]
        nodos=[x[1] for x in G]
        vecinos=[x[2] for x in G]
        nd=buscar(uCodigos, int(nodos[u]))
        v=buscar(uCodigos, int(vecinos[u]))
        if distancias[u]==None:
            distancias[u]=0
        grafo[u].append((distancias[u], nd, v))
        
    return grafo, uCodigos
        




if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1)
    tipoMuestra = {
        'RESTANTES':0,
        'DEPARTAMENTALES':1,
        'PROVINCIALES':2,
        'DISTRITALES':3
    }
    muestra = [] #lista centros poblados
    id = {}
    for cep in centrosPoblados:
        if cep.capital == tipoMuestra['PROVINCIALES']: #es capital departamental
            id[cep.codigo] = cep.codigo
            muestra.append(cep)
            
    G, uCodigos = generarGrafoFloyd(muestra)
    Gmapa=generarGrafo(muestra)
    tamano=len(muestra)
    #print(G)

    caminoFloyd = floydWarshall(G, tamano)
    #print(caminoFloyd)

    #camino=[]
    #construirCamino(caminoFloyd, 0, 23,camino)
    
    arbol=creandoArbol(caminoFloyd, uCodigos, 0, 150)
    #print(arbol)



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


    def pintarAristas(aristas,color):
        for arista in aristas:
            print(arista)
            _,origen,destino = arista
            o = buscarCentroPoblado(origen)
            d = buscarCentroPoblado(destino)
            if o!=None and d!=None:
                x = [o.coordX,d.coordX]
                y = [o.coordY,d.coordY]
                plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")


    #Pintar grafo
    pintarAristas(Gmapa,"blue")
    #Pintar arbol de expansion minima
    pintarAristas(arbol,"white")
    plt.show()
    
