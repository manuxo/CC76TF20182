"""
    Manuel
"""
import heapq as hq
from unionfind import union,find

def kruskal(G,id):
    aristas = []
    resultado = []
    for arista in G:
        costo,nodo,vecino = arista
        hq.heappush(aristas,(costo,nodo,vecino))

    while len(aristas):
        costo,u,v = hq.heappop(aristas)
        pu = find(id,u)
        pv = find(id,v)
        if pu != pv:
            resultado.append((costo,u,v))
            union(id,pu,pv)
    return resultado

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from Leer import leerDataSet,leerArchivo
    from generarGrafo import generarGrafo
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
    G = generarGrafo(muestra)
    arbolExpMin = kruskal(G,id)
    print(arbolExpMin)
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
    plt.show()