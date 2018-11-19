# CC76TF20182
Trabajo final para el curso de Complejidad Algorítmica. UPC - Universidad Peruana de Ciencias Aplicadas

Integrantes: 

• Alvarado Estanga, Manuel

• Bernal Marchena, Luis Angel

• Galarza Rosales, Pablo J.

## Introducción
A lo largo de la existencia de las computadoras, se ha considerado a estas como herramientas de las cuales nos podemos valer para facilitar nuestras actividades. Así, se ha pensado que las computadoras nos pueden ayudar a resolver todos nuestros problemas y que poseen más poder para procesar datos que nosotros. Es raro pensar en que las computadoras poseen limites en sus facultades de cálculo, ya que muy pocas veces nos encontramos ante tales limites; de hecho, probablemente el usuario promedio no tenga que lidiar nunca en su vida con ningún problema que requiera llevar el poder de procesamiento de la computadora hasta casi el límite. Pese a esto, hasta el día de hoy existen ciertos problemas que no han podido ser resueltos ni con la ayuda de las computadoras, esto se debe a que quizás si se pueda encontrar una respuesta, pero el tiempo que le llevaría a las computadoras darnos el resultado podría ser de hasta millones de años.

### P vs NP
Por esta razón se plantea el problema P vs. NP; este problema es considerado como uno de los tantos problemas del millón de dólares. Este problema consiste en comprobar que los problemas NP pueden ser resueltos de igual forma que los polinómicos(P) aplicando diversos conceptos que permitan facilitar el proceso de resolución. Este problema trata de aclarar que problemas pueden resolverse con la ayuda de la computadora y cuales no, para de esta forma determinar si la resolución de dichos problemas se hallará relacionada a la creación de equipos más con más potencia de análisis.

 - P: Las soluciones pueden ser calculadas en un tiempo razonable
 - NP: Las soluciones son muy dificiles de encontrar, pero son fáciles de comprobar

El reto es demostrar que P = NP o lo contrario; es decir, mientras no se pruebe que son diferentes podrían existir atajos que permitan resolver un problema de clase NP como uno de complejidad P. Demostrar que P = NP tendría grandes impactos en la criptografía moderna y haría vulnerables a todos los sistemas a nivel mundial en el caso que sea cierto.

![Gráfico P vs NP](https://qph.fs.quoracdn.net/main-qimg-29c826310da7fed7e085181bafc99598)
Fuente: [Quora - Does P ! = NP mean that no problem exists which can be solved and checked in polynomial time?](https://www.quora.com/Does-P-NP-mean-that-no-problem-exists-which-can-be-solved-and-checked-in-polynomial-time)

### TSP - Travelling Salesman Problem
Entre estos problemas de complejidad NP, se encuentra el problema del vendedor viajero (TSP, por sus siglas en ingles). Dada una colección de ciudades y las distancias entre sus conexiones (costo), el  problema consiste en encontrar un camino que recorra todas las ciudades una única vez y regrese al punto inicial con la menor distancia posible.
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aco_TSP.svg/600px-Aco_TSP.svg.png)
Fuente: [Wikipedia - Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

## Objetivos

• Desarrollar la competencia general de razonamiento cuantitativo y la competencia específica de uso de técnicas y herramientas acorde a los objetivos del curso.

• Desarrollar un algoritmo que permita resolver completa o parcialmente el problema del vendedor viajero.

• Determinar la importancia de la aplicación de algoritmos eficientes a la hora de resolver un problema.

• Analizar la eficiencia y complejidad de los algoritmos planteados.

## Marco Teorico

### Algoritmo de Prim


El resultado de ejecutar el algoritmo de Prim es un arbol de expansion minima, dado un grafo no dirigido y conexo, es decir encuentra un subconjunto de las aristas que formen un arbol que incluya los vertices del grafo inicial, donde el peso total de las aristas es la minima posible.

##### Funcionamiento

1. Se marca un vértice cualquiera. Será el vértice de partida.
2. Se selecciona la arista de menor peso incidente en el vértice seleccionado anteriormente y se selecciona el otro vértice en el que     incide dicha arista.
3. Repetir el paso 2 siempre que la arista elegida enlace un vértice seleccionado y otro que no lo esté. Es decir, siempre que la arista elegida no cree ningún ciclo.
4. El árbol de expansión mínima será encontrado cuando hayan sido seleccionados todos los vértices del grafo.


#### Complejidad

El bucle principal se. ejecuta n- 1 veces, en cada iteración cada bucle interior toma O(n), por lo tanto el tiempo de ejecución del algoritmo de PRIM toma O(n^2 ) . 




### Algoritmo Kruskal

Primero que nada, debemos definir los algoritmos union y find:

Union Find es una estructura de datos que modela una colección de conjuntos disjuntos (disjoint-sets) y esta basado en 2 operaciones:

- Find( A ): Determina a cual conjunto pertenece el elemento A. Esta operación puede ser usada para determinar si 2 elementos están o no en el mismo conjunto.
- Union( A, B ): Une todo el conjunto al que pertenece A con todo el conjunto al que pertenece B, dando como resultado un nuevo conjunto basado en los elementos tanto de A como de B.

#### Metodo Find:

Como se explicó al inicio este método determina a cual componente conexa pertenece un vértice X determinado, ello lo hace retornando el vértice raíz del árbol en el que se encuentra el vértice X.

#### Metodo Union:

Como se explicó al inicio este método me permite unir 2 componentes conexas, ello se realiza por lo siguiente:

1. Obtenemos la raíz del vértice x.
2. Obtenemos la raíz del vértice y.
3. Actualizamos el padre de alguna de las raíces, asignándole como nuevo padre la otra raíz.

#### Funcionamiento Kruskal

Primeramente ordenaremos las aristas del grafo por su peso de menor a mayor. Mediante la técnica greedy Kruskal intentara unir cada arista siempre y cuando no se forme un ciclo, ello se realizará mediante los metodos Union-Find. Como hemos ordenado las aristas por peso comenzaremos con la arista de menor peso, si los vértices que contienen dicha arista no están en la misma componente conexa  entonces los unimos para formar una sola componente mediante Union.

#### Complejidad

La complejidad se puede analizar contemplando lo siguiente:

• Se tiene una complejidad de O(a*log(a)) para ordenar los arcos, el cual es equivalente a O(a*log(a)), como n- 1 <=  a <=    n(n- 1)/2

• Se tiene una complejidad de O( n) al inicializar los n conjuntos disjuntos

• Se tiene una complejidad de 0((2a- 1)log*n para todas las búsquedas

Considerando que:

K llamadas a operaciones buscar el líder del conjunto que contiene a un vértice de conjuntos disjuntos den elementos lleva un tiempo de O(Klog*n).

log*n E O(logn), pero logn ~ O(log*n).

Por lo tanto podemos concluir que la complejidad del algoritmo de Kruskal es O(a*log(n)). 



### Algoritmo Floyd-Warshall

Fue descrito por primera vez por Bernard Roy en 1959, se trata de un algoritmo de análisis sobre grafos para encontrar el camino minimo en grafos dirigidos. Este algoritmo encuentra el mejor camino de todos los pares de vertices en una sola ejecución y es un claro ejemplo de programación dinamica.

Este algoritmo a su vez se trata de la mezcla de dos distintos algoritmos, los cuales son indicados en su nombre compuesto; así pues, para entender aún más el funcionamiento de este algoritmo se presentará una breve explicación de los algoritmos que lo componen:

### Algoritmo de Warshall

Es un algoritmo booleano, ya que hace uso de una matriz compuesta de 0 e 1, los cuales indican que hay o no correspondencia en el grafo y, a travez de este algoritmo se obtiene una matriz transitiva la cual muestra si es que dos nodos se hallan conectados mediante una union indirecta.

### Algoritmo de Floyd

Es bastante similar al algoritmo usado por Warshall, pero este permite el uso de grafos ponderados, permitiendo que la "flecha" que indica la union entre dos nodos tenga valores enteros o infinito, siendo infinito un indicador de que esos nodos no poseen una union directa entre ellos. De esta forma, este algoritmo es perfectamente aplicable para las distancias almacenadas entre cada par de nodos que se encuentren conectados.

### Funcionamiento Floyd-Warshall

Este algoritmo compara todos los posibles caminos entre cada par de vertices que se encuentra en el grafo en tan solo V^3 comparaciones, lo cual es logrado gracias a que poco a poco hace una estimación del mejor camino entre dos vértices, hasta que se sabe la estimación optima.

Se define un grafo G con vertices V numerados de 1 a N, y una funcion CaminoMinimo(i, j, k) que devuelve el camino minimo de i a j (los cuales conforman V) utilizando solo los vertices de 1 a k como puntos intermedios en el camino. Dada esta función se procede a calcular el camino minimo de i a j utilizando solo los vertices de 1 hasta a k+1.

Una vez definido esto, se pueden presentar dos posibles situaciones; el camino minimo se puede hallar directamente mediante la funcion CaminoMinimo(i, j, k) y se halla comprendido entre los vertices 1 a k+1; o se encuentra como el camino minimo de k+1 a j, por lo cual se debiesen de concatenar dos caminos minimos para formar el más optimo.

### Complejidad de Floyd-Warshall

La complejidad de este algoritmo es O(n^3) . El algoritmo resuelve eficientemente la búsqueda de todos los caminos más cortos entre cualesquiera nodos. Sin embargo, la busqueda se vuelve lenta.


## Experimentación

### Solución 1: Aplicando el algoritmo Kruskal

Para esta solución utilizaremos el algoritmo de kruskal para hallar árboles de expansión mínima. En primer lugar, se obtendrán los datos de todos los centros poblados desde un archivo con extensión csv. Para ello definimos el siguiente modelo:
```python 
	#Clase CentroPoblado
	class  CentroPoblado:
		def  __init__(self,codigo,nombre,departamento,provincia,distrito,capital,coordX, coordY):
			self.codigo = codigo
			self.nombre = nombre
			self.departamento = departamento
			self.provincia = provincia
			self.distrito = distrito
			self.capital = capital
			self.coordX = coordX
			self.coordY = coordY
		def  __str__(self):
			return  "%s D: %s P: %s D: %s Cap: %d Cod: %s X: %f Y: %f"  % (self.nombre, self.departamento, self.provincia, self.distrito, self.capital, self.codigo,self.coordX,self.coordY)
```
Luego, definimos una función para leer el dataset:
```python
	def  leerDataSet(nombreArchivo,inicio,fin  =  0):
		centrosPoblados = []
		try:
			archivo =  open(nombreArchivo)
			lineas = archivo.readlines()
			if fin !=  0:
				lineas = lineas[inicio:(fin+1)]
			else:
				lineas = lineas[inicio:]
			registros = []
			for linea in lineas:
				aux = linea.replace('\n','')
				if  len(aux.split(',')) ==  18: #valida si el registro tiene 18 columnas
					registros.append(aux)
			print(len(registros))
			for registro in registros:
				datos = registro.split(',')
				departamento,provincia,distrito,codigo,nombre = datos[1:6]
				capital =  int(datos[7])
				coordX,coordY = datos[15:17]
				coordX =  float(coordX)
				coordY =  float(coordY)
					centrosPoblados.append(CentroPoblado(codigo,nombre,departamento,provincia,distrito,capital,coordX,coordY))
		except  FileNotFoundError:
			print("Archivo no encontrado.")
		finally:
			archivo.close()
			return centrosPoblados
 ```
Implementamos el algoritmo de Kruskal en python:
```python
def  kruskal(G,id):
	aristas = []
	resultado = []
	for arista in G:
		costo,nodo,vecino = arista
		hq.heappush(aristas,(costo,nodo,vecino))
	while  len(aristas):
		costo,u,v = hq.heappop(aristas)
		pu = find(id,u)
		pv = find(id,v)
		if pu != pv:
			resultado.append((costo,u,v))
			union(id,pu,pv)
	return resultado
 ```
Finalmente, aplicamos el algoritmo para una muestra:
``` python
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
id  = {}
for cep in centrosPoblados:
	if cep.capital == tipoMuestra['DEPARTAMENTALES']:
		id[cep.codigo] = cep.codigo
		muestra.append(cep)
G = generarGrafo(muestra)
arbolExpMin = kruskal(G,id)
print(arbolExpMin)
```

##### Resultados
Estos fueron los resultados obtenidos durante la experimentación:

 - [x] Aplicar su solución a las 25 capitales departamentales.
 ![Prueba en departamentales](https://i.imgur.com/q7ri8Ki.png)
 - [x] Aplicar su solución a las 171 capitales provinciales
 ![Prueba en provinciales](https://i.imgur.com/8s9P4wu.png)
 - [x] Aplicar su solución a las 1’678 capitales distritales.
 ![Prueba en distritales](https://i.imgur.com/Q0S16t3.png)
 - [ ] Aplicar su solución a los 143’351 centros poblados restantes
No fue posible aplicar este algoritmo en un tiempo razonable para dicha muestra.

### Solución 2: Aplicando el algoritmo de Prim

Para la solucion 2 se utilizo el algoritmo Prim:

En primer lugar se crearon diccionarios para las distancias, padres y visitados. Luego se creo un arreglo vacio y en él se agregaron las distancias y los vertices.
```python 
def prim(G,centrosPoblados,inicio = 0):
    #lista de aristas
    resultado = []

    dist = {}
    for cep in centrosPoblados:
        dist[cep.codigo] = math.inf
    padres = {}
    for cep in centrosPoblados:
        padres[cep.codigo] = ''
    visitados = {}
    for cep in centrosPoblados:
        visitados[cep.codigo] = False
    q = []
    hq.heappush(q, (0,centrosPoblados[inicio].codigo))
```
Luego se implemento el algoritmo Prim, donde se retorna un grafo de padres, distancias y el grafo resultante.
```python 
	while len(q) > 0:
        _,u = hq.heappop(q)
        if not visitados[u]:
            visitados[u] = True
            for w,v in G[u]:
                if not visitados[v] and w < dist[v]:
                    dist[v] = w
                    padres[v] = u
                    resultado.append((u,v))
                    hq.heappush(q, (w,v))
    return padres,dist,resultado
```
Finalmente se uso el algoritmo para una muestra:

```python 
    centrosPoblados = leerDataSet("dataset.csv",1)
    tipoMuestra = {
        'RESTANTES':0,
        'DEPARTAMENTALES':1,
        'PROVINCIALES':2,
        'DISTRITALES':3
    }
    muestra = []
    for cep in centrosPoblados:
        if cep.capital == tipoMuestra['DEPARTAMENTALES']:
            muestra.append(cep)
    grafo = generarGrafo(muestra)
    padres,distancias,resultado = prim(grafo,muestra)
    print(resultado)

```

##### Resultados
Estos fueron los resultados obtenidos durante la experimentación:

 - [x] Aplicar su solución a las 25 capitales departamentales.
 ![Prueba en departamentales](https://i.imgur.com/CTsenrt.png)
 - [x] Aplicar su solución a las 171 capitales provinciales
 ![Prueba en provinciales](https://i.imgur.com/ygLlsv5.png)
 - [x] Aplicar su solución a las 1’678 capitales distritales.
 ![Prueba en distritales](https://i.imgur.com/g3fTA3D.png)
 - [ ] Aplicar su solución a los 143’351 centros poblados restantes
No fue posible aplicar este algoritmo en un tiempo razonable para dicha muestra.

### Solución 3: Aplicando el algoritmo Floyd-Warshall

Para esta solución se implementará una matriz que almacene todos los mejores caminos para llegar a todos los nodos con que se cuenta. En primer lugar, se generá un grafo común utilizando el data set creado anteriormente:

 ```python
 def generarGrafo(centrosPoblados):
    grafo = []
    
    for cep in centrosPoblados:
        copia = centrosPoblados[:] # genera una copia de todos los centros poblados
        copia.remove(cep) #removemos el cep seleccionado para no generar un camino al mismo punto
        destinosPorCep = random.randint(3,5) # seleccionamos entre 3 y 5 destinos por cada centro poblado
        for _ in range(destinosPorCep):
            destino = random.choice(copia) #seleccionamos un destino al azar
            copia.remove(destino) #removemos el destino para que no se repita
            #Generamos una nueva arista
            distancia = calcularDistancia(cep,destino)
            arista = (distancia,cep.codigo,destino.codigo)
            grafo.append(arista)
    return grafo
  ```
  
Ya que se va a trabajar con matrices, este grafo generado se ve cambiado para fines de mejor manejo, reemplazando los codigos reales de los nodos por numeros mas pequeños desde 0 a n-1 nodos:

```python
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
```

De esta funcion se obtiene un nuevo grafo que ya puede ser procesado por nuestro algoritmo Floyd-Warshall y un arreglo que contiene los codigos reales y sus números ahora asignados. A continuación se utiliza el algoritmo de Floyd-Warshall para obtener la matriz con todos los caminos posibles:

```python
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
```

Finalmente se aplica el algoritmo, obteniendo así la matriz deseada con los resultados:

```python
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
    caminoFloyd = floydWarshall(G, tamano)
    print(caminoFloyd)
```
## Conclusiones

Finalmente, se puede concluir que al momento de la ejecucion de los algoritmos Prim y Kruskal:

• Ambos algoritmos se pudieron ejecutar de manera satisfactoria y rapida para las muestras de Departamentos, Provincias y Distrital

• Si se ejecutara el algoritmo para las muestras restantes, es decir para todos los centros poblados, se mostraria los resultados adecuados. Sin embargo, el tiempo de ejecucion seria muy extenso, lo cual no es lo mas optimo.
	
## Bibliografia:

Complejidad Algoritmica(2016) Algoritmo de Prim (Recuperado de: https://sites.google.com/site/complejidadalgoritmicaes/prim) 
(fecha de consulta: 17 de noviembre del 2017)

Algorithms and more(2012) Disjoint-set: Union Find (Recuperado de: https://jariasf.wordpress.com/2012/04/02/disjoint-set-union-find/) 
(fecha de consulta: 17 de noviembre del 2017)

Algorithms and more(2012) Arbol de expansion minima: Algoritmo de Kruskal (Recuperado de: https://jariasf.wordpress.com/2012/04/19/arbol-de-expansion-minima-algoritmo-de-kruskal/) (fecha de consulta: 17 de noviembre del 2017)

Cubana, E. Floyd-Warshall . Obtenido de https://www.ecured.cu/Floyd-Warshall (fecha de consulta: 18 de noviembre de 2018)

II, E. d. Algoritmo de Floyd-Warshall. Obtenido de https://estructurasite.wordpress.com/algortimo-de-floyd-warshall/ (fecha de consulta: 18 de noviembre de 2018)

Wikipedia. Algoritmo de Floyd-Warshall. Obtenido de https://es.wikipedia.org/wiki/Algoritmo_de_Floyd-Warshall (fecha de consulta: 18 de noviembre de 2018)

Tocto, P (2012) Comparacion algoritmo Prim y Kruskal(Recuperado de: http://cybertesis.uni.edu.pe/bitstream/uni/3416/1/tocto_ip.pdf)
(fecha de consulta: 18 de noviembre de 2018)

Herrera, S.(2014) Eficiencia algorítmica en aplicaciones de grafos orientadas
a redes GMPLS (Recuperado de: http://www.scielo.org.co/pdf/rfing/v23n36/v23n36a09.pdf) (fecha de consulta: 18 de noviembre de 2018)
