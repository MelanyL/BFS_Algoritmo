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
    
    def Imprimir_lista_adyacencia(self):
        """
        El método permite imprimir el grafo generado a través de la lista de adyacencia.
        """
        # recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # imprime cada nodo almacenado en la lista de adyacencia.
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
    
    def bfs_transversal(self, nodo_de_inicio):
        """
        Este método permite insertar el recorrido BFS de un nodo inicial, posteriormente genera una lista de colas visitadas y muestra el recorrido realizado hasta llegar al objetivo deseado. 

        Parametros -----> nodo_de_inicio : int
                          visitado : int
                          cola : int
        """
        visitado = set()
        cola = Queue()

        # permite asignar los nodos visitados a la cola para evitar bucles
        cola.put(nodo_de_inicio)

        # Permite añadir el nodo_de_inicio a la lista de visitas
        visitado.add(nodo_de_inicio)

        # Bucle de los nodos que se ejecutara si la cola no se encuentra vacia.
        while not cola.empty():
            # Asigna el nodo de la cola al nodo_actual
            nodo_actual = cola.get()
            # Imprime los nodos.
            print(nodo_actual, end=" ")

            # Bucle de obtención del siguiente nodo de la lista de adyacencia
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                # En caso de que un nodo adyaente haya sido visitado
                if siguiente_nodo not in visitado:
                    # Se agrega el nodo a la cola
                    cola.put(siguiente_nodo)
                    # Se agrega el nodo a la lista de visitados
                    visitado.add(siguiente_nodo)

if __name__ == "__main__":

    """
    En la clase main se instancia la clase Grafo para acceder a sus metodos, posteriormente se elaboran 5 casos de prueba para comprobar el funcionamiento del programa.
    """
    
    print(" Caso de Prueba 1")
    grafo1 = Grafo(6, dirigido = False) # Se procede a instanciar la clase `Grafo`.
    grafo1.agregar_borde(0, 1, 2) # Se asigna los bordes
    grafo1.agregar_borde(0, 2, 3) # Se asigna los bordes
    grafo1.agregar_borde(0, 3, 5) # Se asigna los bordes
    grafo1.agregar_borde(2, 4, 4) # Se asigna los bordes
    grafo1.agregar_borde(2, 5, 8) # Se asigna los bordes

    grafo1.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia
 
    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    grafo1.bfs_transversal(0)
    print()

    print(" Caso de Prueba 2")
    grafo2 = Grafo(6, dirigido = False) # instancia de la clase 'Grafo'
    grafo2.agregar_borde(0, 1, 5) # Se agrega los bordes
    grafo2.agregar_borde(0, 2, 2) # Se agrega los bordes
    grafo2.agregar_borde(0, 3, 3) # Se agrega los bordes
    grafo2.agregar_borde(1, 2, 7) # Se agrega los bordes
    grafo2.agregar_borde(1, 4, 5) # Se agrega los bordes
    grafo2.agregar_borde(2, 3, 6) # Se agrega los bordes
    grafo2.agregar_borde(2, 4, 2) # Se agrega los bordes
    grafo2.agregar_borde(2, 5, 2) # Se agrega los bordes    
    

    grafo2.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia

    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    grafo2.bfs_transversal(0)
    print()

    print(" Caso de Prueba 3")
    grafo3 = Grafo(4, dirigido = False) # instancia de la clase `Grafo`
    grafo3.agregar_borde(0, 1, 3) # Se agrega los bordes
    grafo3.agregar_borde(0, 2, 1) # Se agrega los bordes
    grafo3.agregar_borde(0, 3, 2) # Se agrega los bordes
    grafo3.agregar_borde(1, 2, 4) # Se agrega los bordes
    grafo3.agregar_borde(2, 3, 5) # Se agrega los bordes

    grafo3.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia

    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    grafo3.bfs_transversal(0)
    print()