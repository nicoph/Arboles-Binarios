### Versión complejizada del arbol, le agregue unos métodos para poder visualizarlo y sacar promedio por nivel
### ya que cada nodo no solo tiene valor , sino que también nivel


class Nodo:
    def __init__(self, valor, nivel):
        self.valor = valor
        self.nivel = nivel
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor):
        if type(valor) != int or valor <= 0:
            print("El valor del nodo debe ser un entero positivo.")
            return
        if self.raiz is None:
            self.raiz = Nodo(valor, 0)
        else:
            self._agregar_nodo_recursivo(valor, self.raiz, 1)

    def _agregar_nodo_recursivo(self, valor, nodo_actual, nivel):
        if nodo_actual.izquierdo is None:
            nodo_actual.izquierdo = Nodo(valor, nivel)
        elif nodo_actual.derecho is None:
            nodo_actual.derecho = Nodo(valor, nivel)
        else:
            if nodo_actual.izquierdo.izquierdo is None or nodo_actual.izquierdo.derecho is None:
                self._agregar_nodo_recursivo(valor, nodo_actual.izquierdo, nivel + 1)
            else:
                self._agregar_nodo_recursivo(valor, nodo_actual.derecho, nivel + 1)

    def ver_nodo(self, valor):
        return self._ver_nodo_recursivo(valor, self.raiz)

    def _ver_nodo_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return None
        if nodo_actual.valor == valor:
            return nodo_actual
        nodo_izquierdo = self._ver_nodo_recursivo(valor, nodo_actual.izquierdo)
        if nodo_izquierdo:
            return nodo_izquierdo
        nodo_derecho = self._ver_nodo_recursivo(valor, nodo_actual.derecho)
        if nodo_derecho:
            return nodo_derecho
        return None

    def establecer_valor(self, valor, nuevo_valor):
        nodo = self.ver_nodo(valor)
        if nodo is not None:
            nodo.valor = nuevo_valor
            
    def visualizar_arbol(self):
        self._visualizar_arbol_recursivo(self.raiz, 0)

    def _visualizar_arbol_recursivo(self, nodo, nivel):
        if nodo is None:
            return
        self._visualizar_arbol_recursivo(nodo.derecho, nivel + 1)
        print("   |" * nivel + "__" + str(nodo.valor))
        self._visualizar_arbol_recursivo(nodo.izquierdo, nivel + 1)
        
    def promedio_nivel(self, nivel=None):
        if nivel is None:
            suma, cantidad = self._sumar_nodos(self.raiz)
        else:
            suma, cantidad = self._sumar_nodos_nivel(self.raiz, nivel, 0)
        if cantidad > 0:
            return suma / cantidad
        else:
            return None

    def _sumar_nodos(self, nodo_actual):
        if nodo_actual is None:
            return 0, 0
        suma_izquierdo, cantidad_izquierdo = self._sumar_nodos(nodo_actual.izquierdo)
        suma_derecho, cantidad_derecho = self._sumar_nodos(nodo_actual.derecho)
        suma = suma_izquierdo + suma_derecho + nodo_actual.valor
        cantidad = cantidad_izquierdo + cantidad_derecho + 1
        return suma, cantidad

    def _sumar_nodos_nivel(self, nodo_actual, nivel_objetivo, nivel_actual):
        if nodo_actual is None:
            return 0, 0
        if nivel_actual == nivel_objetivo:
            return nodo_actual.valor, 1
        suma_izquierdo, cantidad_izquierdo = self._sumar_nodos_nivel(nodo_actual.izquierdo, nivel_objetivo, nivel_actual + 1)
        suma_derecho, cantidad_derecho = self._sumar_nodos_nivel(nodo_actual.derecho, nivel_objetivo, nivel_actual + 1)
        return suma_izquierdo + suma_derecho, cantidad_izquierdo + cantidad_derecho

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo_actual):
        if nodo_actual is None:
            return -1
        altura_izquierdo = self._calcular_altura(nodo_actual.izquierdo)
        altura_derecho = self._calcular_altura(nodo_actual.derecho)
        return max(altura_izquierdo, altura_derecho) + 1