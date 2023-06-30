
from Arbol import ArbolBinario
from Arbol_simple import ArbolBinarioSimple
import random

## arbol complejo
arbol = ArbolBinario()

#funcion crear para arbol 1

def crear_arbol(n):
    
    for x in range(n):
        arbol.agregar_nodo(random.choice(range(n)))

#test Arbol binario 1
crear_arbol(10)
# visualizar y sacar promedio
print('\n ### Arbol ###\n')

arbol.visualizar_arbol()
print(arbol.promedio_nivel())


#test arbol 2, verión simple
print('\n', '### Arbol simple ###\n')
arbols=ArbolBinarioSimple()
arbols.completar_arbol(20)

print(arbols.ver_nodos())
print(arbols.promedio_arbol())