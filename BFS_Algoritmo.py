# Importamos la libreria Queue
from queue import Queue

#Creamos la clase denominada Grafo
class Grafo():
    """
    En esta clase mostrará a un grafo en conjunto con sus atributos y métodos respectivas de este, los atributos son los siguientes:

    Atributos:
        m_numero_nodos : int -----> Cantidad de nodos que contendrá el gráfo.
        m_nodos : int -----> Rango de nodos en donde trabajará el gráfo.
        m_dirigido : boolean ------> Tipo de nodo ya sea dirigido o no dirigido.
        m_lista_adyacencia : diccionario ------> Diccionario que almacena el valor de los nodos de la lista de adyacencia. 

    Métodos:

        __init__(self, num_de_nodos, dirigido=True), este método hará la función de constuctor de la clase denominada 'Grafo()', en donde recepta el número de nodos (m_num_nodos), y posteriormente crea el rango de nodos (numero_nodos), a continuación, determina el tipo de grafo si es dirigido o no dirigido dependiendo del caso (m_dirigido) y para finalizar se creará el diccionario de la lista de adyacencia.

        agregar_borde(self, nodo1, nodo2, peso=1), este método genera los bordes de la lista de adyacencia asignando el nodo 2 a la lista de adyacencia del nodo 1.

        Imprimir_lista_adyacencia(self), este método permite imprimir el grafo generado en base a la lista de adyacencia, bfs_transversal(self, nodo_de_inicio), este método imprime el recorrido BFS de un vértice fuente dado de la lista de adyacencia.
    """
    def __init__(self, numero_nodos, dirigido=True):
        """
        Este método hará la función de constuctor de la clase denominada 'Grafo()', en donde recepta el número de nodos (m_num_nodos), y posteriormente crea el rango de nodos (numero_nodos), a continuación, determina el tipo de grafo si es dirigido o no dirigido dependiendo del caso (m_dirigido) y para finalizar se creará el diccionario de la lista de adyacencia.

        Atributos:
        m_numero_nodos : int -----> Cantidad de nodos que contendrá el gráfo.
        m_nodos : int -----> Rango de nodos en donde trabajará el gráfo.
        m_dirigido : boolean ------> Tipo de nodo ya sea dirigido o no dirigido.
        m_lista_adyacencia : diccionario ------> Diccionario que almacena el valor de los nodos de la lista de adyacencia. 
        """
        # Asignamos el valor del numero de nodos por medio del parámetro receptado.
        self.m_numero_nodos = numero_nodos
        # Se genera el rango de nodos en base a m_numero_nodos
        self.m_nodos = range(self.m_numero_nodos)
        # Se establece el tipo de grafo
        self.m_dirigido = dirigido
        # Se crea el diccionario respectivo de la lista de adyacencia
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    def agregar_borde(self, nodo1, nodo2, peso=1):
        """
        Este método define el borde respectivo de la lista de adyacencia, y recepta como parametros: el nodo1, el nodo2 y el peso que tiene un valor por defecto es de 1.
        Posteriormente se agregan a la lista de adyacencia del nodo al que corresponde.

        Parametros -----> nodo1 : int
                          nodo2 : int
                          peso: int
        """
        # Se agrega el nodo 2 a la lista de adyacencia del nodo 1.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        if not self.m_dirigido:
            # Se agrega el nodo 1 a la lista de adyacencia del nodo 2.
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
