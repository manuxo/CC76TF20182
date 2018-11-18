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
        
        registros = []
        i = 0
        for linea in lineas:
            aux = linea.replace('\n','')
            if len(aux.split(',')) == 18: #valida si el registro tiene 18 columnas
                registros.append(aux)
            i += 1

        print(len(registros))
        for registro in registros:
            datos = registro.split(',')
            departamento,provincia,distrito,codigo,nombre = datos[1:6]
            capital = int(datos[7])
            coordX,coordY = datos[15:17]
            coordX = float(coordX)
            coordY = float(coordY)
            centrosPoblados.append(CentroPoblado(codigo,nombre,departamento,provincia,distrito,capital,coordX,coordY))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
        return centrosPoblados


if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1)
    i = 0
    for cep in centrosPoblados:
        if cep.capital == 1: #imprime capitales departamentales
            print(cep)
            i+=1
    print("Total capitales departamentales: " + str(i))
