from models.CentroPoblado import CentroPoblado


def leerArchivo(nombreArchivo):
    datos = []
    try:
        archivo = open(nombreArchivo)
        lineas = archivo.readlines()
        for linea in lineas:
            datos.append(linea.replace('\n',''))
    except FileNotFoundError:
        print("Archivo no encontrado")
    finally:
        archivo.close()
        return datos

def leerDataSet(nombreArchivo,inicio,fin = 0):
    centrosPoblados = []
    try:
        archivo = open(nombreArchivo)
        lineas = archivo.readlines()
        if fin != 0:
            lineas = lineas[inicio:(fin+1)]
        else:
            lineas = lineas[inicio:]
        registros = [None] * len(lineas)
        i = 0
        for linea in lineas:
            registros[i] = linea.replace('\n','')
            i += 1
        for registro in registros:
            datos = registro.split(',')
            departamento,provincia,distrito,codigo,nombre = datos[1:6]
            coordX,coordY = datos[15:17]
            coordX = float(coordX)
            coordY = float(coordY)
            centroPoblado = CentroPoblado(codigo,nombre,departamento,provincia,distrito,coordX,coordY)
            centrosPoblados.append(centroPoblado)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        if archivo != None:
            archivo.close()
        return centrosPoblados

if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1)

    for cep in centrosPoblados:
        print(cep)