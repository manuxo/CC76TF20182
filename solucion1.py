"""
    Manuel
"""
from Leer import leerDataSet,leerArchivo

if __name__ == "__main__":
    centrosPoblados = leerDataSet("dataset.csv",1,5)
    
    for cep in centrosPoblados:
        print(cep)

    departamentos = leerArchivo("departamentos.txt")

    print(departamentos)