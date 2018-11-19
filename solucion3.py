"""
Luis Angel
"""
import math
import matplotlib.pyplot as plt
from Leer import leerDataSet,leerArchivo
from generarGrafo import generarGrafo
from itertools import groupby


def camino(maPadres, inicio, fin):
    d=[]
    d.append(inicio)
    while(maPadres[inicio][fin]!=inicio):
        if maPadres[inicio][fin]==-1:
            print('No existe tal camino')
            n=len(d)
            for u in range(n):
                d.pop()
            break
        d.append(maPadres[inicio][fin])
        tmpfin=maPadres[inicio][fin]
        tmpinicio=inicio
        while(maPadres[tmpinicio][tmpfin]!=tmpinicio):
            d.append(maPadres[tmpinicio][tmpfin])
            inicio=maPadres[tmpinicio][tmpfin]
        inicio=maPadres[inicio][fin]
        
    d.append(fin)
    if maPadres[inicio][fin]==-1:
        d.pop()
    
    return d



def transformar(uCodigos, buscado):
    n=len(uCodigos)
    for nro, nodo in uCodigos:
        if nro==buscado:
            return nodo
        else:
            return 0
    
def creandoArbol(maPadres, uCodigos):
    resultado=[]
    d=camino(maPadres, 0, 1)
    n=len(d)
    for u in range(n):
        nodo=transformar(uCodigos, d[u])
        if u+1!=n:
            vecino=transformar(uCodigos, d[u+1])
            resultado.append((0,nodo,vecino))
        else:
            resultado.append((0,nodo,nodo))
            
    return resultado


def floydWarshall(G, tamano):
    n=len(G)
    maCostos = [[math.inf]*tamano for _ in range(tamano)]
    maPadres = [[-1]*tamano for _ in range(tamano)]
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
        if cep.capital == tipoMuestra['DEPARTAMENTALES']: #es capital departamental
            id[cep.codigo] = cep.codigo
            muestra.append(cep)
            
    G, uCodigos = generarGrafoFloyd(muestra)
    tamano=len(muestra)
    #print(G)
<<<<<<< HEAD
    caminoFloyd = floydWarshall(G, tamano)
    #print(caminoFloyd)
    #print(len(caminoFloyd))
    """
=======
    caminoFloyd = floydWarshall(G)
    print(caminoFloyd)
>>>>>>> b25ade3da97165381945394a26fb5db0455e92a6
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
    """
    def buscarCentroPoblado(codigo):
        for cep in centrosPoblados:
            if cep.codigo == codigo:
                return cep


    def pintarAristas(aristas,color):
        for arista in aristas:
            _,origen,destino = arista
            o = buscarCentroPoblado(origen)
            d = buscarCentroPoblado(destino)
            x = [o.coordX,d.coordX]
            y = [o.coordY,d.coordY]
            plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")
  

    #Pintar grafo
        pintarAristas(G,"blue")
        #Pintar arbol de expansion minima
        pintarAristas(arbolExpMin,"white")
    """
    #print(G)
    #print(caminoFloyd)
    destinos=camino(caminoFloyd, 1, 2)
    print(destinos)
    plt.show()

    
   