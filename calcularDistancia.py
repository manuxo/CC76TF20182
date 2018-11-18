import math

def calcularDistancia(cepOrigen,cepDestino):
    resX = cepDestino.coordX - cepOrigen.coordX
    resY = cepDestino.coordY - cepOrigen.coordY
    resX2 = resX ** 2
    resY2 = resY ** 2
    dist = math.sqrt(resX2 + resY2)
    return dist