from clases.nodo import *
from clases.arbolb import *

# -----------------
# Comienzo del programa principal de Árbol Binario de Búsqueda

#lista = [15, 9, 20, 6, 10, 19, 22, 80, 20, 10, 5, 40, 9, 40]
lista =[20,15,24,10,17,22,28,9,11,18,16,21,23,29,27]
miarbol = ArbolBB()
for i in range(len(lista)):
    nodoaux = Nodo(lista[i])
    miarbol.insertarInformado(Nodo(lista[i]))
    #print(nodoaux, end=" ")
print("\nRecorrido preorden")
miarbol.recorridopreorden()
print("\nRecorrido inorden")
miarbol.recorridoinorden()
print("\nRecorrido posorden")
miarbol.recorridoposorden()
print("\nRecorrido anchura")
miarbol.recorridoanchura()
print("\n\nLa profundidad del árbol es", miarbol.calculaprofundidad())

nodoaux = miarbol.buscarInformado(10) # Devuelve la referencia al nodo encontrado.

if nodoaux != None:
    print("Hemos devuelto en la variable nodoaux el nodo que contiene el valor", nodoaux)
    miarbol.preorden(nodoaux)
else:
    print("Lamentamente, el árbol no contiene un nodo no está en el árbol")