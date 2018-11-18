# CC76TF20182
Trabajo final para el curso de Complejidad Algorítmica. UPC - Universidad Peruana de Ciencias Aplicadas



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

### Bibliografia:

https://sites.google.com/site/complejidadalgoritmicaes/prim

https://jariasf.wordpress.com/2012/04/02/disjoint-set-union-find/

https://jariasf.wordpress.com/2012/04/19/arbol-de-expansion-minima-algoritmo-de-kruskal/
