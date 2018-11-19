# CC76TF20182
Trabajo final para el curso de Complejidad Algorítmica. UPC - Universidad Peruana de Ciencias Aplicadas

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

## Marco Teorico

### Algoritmo de Prim


El resultado de ejecutar el algoritmo de Prim es un arbol de expansion minima, dado un grafo no dirigido y conexo, es decir encuentra un subconjunto de las aristas que formen un arbol que incluya los vertices del grafo inicial, donde el peso total de las aristas es la minima posible.

##### Funcionamiento

1. Se marca un vértice cualquiera. Será el vértice de partida.
2. Se selecciona la arista de menor peso incidente en el vértice seleccionado anteriormente y se selecciona el otro vértice en el que     incide dicha arista.
3. Repetir el paso 2 siempre que la arista elegida enlace un vértice seleccionado y otro que no lo esté. Es decir, siempre que la arista elegida no cree ningún ciclo.
4. El árbol de expansión mínima será encontrado cuando hayan sido seleccionados todos los vértices del grafo.


#### Complejidad



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

## Bibliografia:

Complejidad Algoritmica(2016) Algoritmo de Prim (Recuperado de: https://sites.google.com/site/complejidadalgoritmicaes/prim) 
(fecha de consulta: 17 de noviembre del 2017)

Algorithms and more(2012) Disjoint-set: Union Find (Recuperado de: https://jariasf.wordpress.com/2012/04/02/disjoint-set-union-find/) 
(fecha de consulta: 17 de noviembre del 2017)

Algorithms and more(2012) Arbol de expansion minima: Algoritmo de Kruskal (Recuperado de: https://jariasf.wordpress.com/2012/04/19/arbol-de-expansion-minima-algoritmo-de-kruskal/) (fecha de consulta: 17 de noviembre del 2017)
