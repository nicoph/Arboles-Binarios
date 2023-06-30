class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinarioSimple:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor):
        if type(valor) != int or valor <= 0:
            print("El nodo debe ser un entero positivo.")
            return

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_nodo_recursivo(valor, self.raiz)


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

    def ver_nodo(self, valor):
        return self._ver_nodo_recursivo(valor, self.raiz)

    def _ver_nodo_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._ver_nodo_recursivo(valor, nodo_actual.izquierda)
        return self._ver_nodo_recursivo(valor, nodo_actual.derecha)

    def completar_arbol(self, cantidad_nodos):
        import random
        for _ in range(cantidad_nodos):
            self.agregar_nodo(random.randint(1, 100))

    def ver_nodos(self):
        nodos = []
        self._ver_nodos_recursivo(self.raiz, nodos)
        return nodos

    def _ver_nodos_recursivo(self, nodo_actual, nodos):
        if nodo_actual is not None:
            self._ver_nodos_recursivo(nodo_actual.izquierda, nodos)
            nodos.append(nodo_actual.valor)
            self._ver_nodos_recursivo(nodo_actual.derecha, nodos)

    def promedio_arbol(self):
        nodos = self.ver_nodos()
        if nodos:
            return sum(nodos) / len(nodos)
        return 0.0
