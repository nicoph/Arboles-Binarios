class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

## clase nodo donde defino su valor y el enlace a sus dos hijos

class ArbolBinarioSimple:
    def __init__(self):
        self.raiz = None

    ## inicializo un arbol vacio, la raiz en none

    def agregar_nodo(self, valor):
        if type(valor) != int or valor <= 0:
            print("El nodo debe ser un entero positivo.")
            return

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_nodo_recursivo(valor, self.raiz)

    ## para agregar nodo primero me fijo si es entero positivo
    ## despues chequeo si la raiz esta vacia
    ## sino voy a la recursiva

    def _agregar_nodo_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar_nodo_recursivo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar_nodo_recursivo(valor, nodo_actual.derecha)
                
    ## Compara el valor a insertar con el valor del nodo actual. Si es menor, verifica si el nodo izquierdo 
    ##está vacío y, de ser así, crea un nuevo nodo con el valor y lo establece como el nodo izquierdo. 
    ##Si el nodo izquierdo no está vacío, la función se llama a sí misma de manera recursiva con el nodo izquierdo como parámetro.
    ##Si el valor es mayor o igual, se realiza un proceso similar pero con el nodo derecho.
    
    
    def ver_nodo(self, valor):
        return self._ver_nodo_recursivo(valor, self.raiz)

    def _ver_nodo_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._ver_nodo_recursivo(valor, nodo_actual.izquierda)
        return self._ver_nodo_recursivo(valor, nodo_actual.derecha)

    ## puse ver nodo para traer un nodo solo , la recursiva me permite buscar un nodo del valor q paso como parametro
    # lo iba a usar para un metodo de busqueda pero no me dio el tiempo

    def ver_nodos(self):
        nodos = []
        self._ver_nodos_recursivo(self.raiz, nodos)
        return nodos

    def _ver_nodos_recursivo(self, nodo_actual, nodos):
        if nodo_actual is not None:
            self._ver_nodos_recursivo(nodo_actual.izquierda, nodos)
            nodos.append(nodo_actual.valor)
            self._ver_nodos_recursivo(nodo_actual.derecha, nodos)
            
    ### el ver nodos lo uso para sacar una lista de todos los nodos y hacer el promedio

    def completar_arbol(self, cantidad_nodos):
        import random
        for _ in range(cantidad_nodos):
            self.agregar_nodo(random.randint(1, 10))
            
    def promedio_arbol(self):
        #return mean(self.ver_nodos())
        nodos = self.ver_nodos()
        if nodos:
            return sum(nodos) / len(nodos)
        return 0.0
