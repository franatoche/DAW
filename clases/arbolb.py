from queue import *

class ArbolBB(object):
    def __init__(self, raiz=None):
        self._raiz = raiz

    def insertarInformado(self, nodo):
        if self._raiz == None:
            self._raiz = nodo
        else:
            aux = self._raiz
            while True:
                if (nodo.getValor() <= aux.getValor()):
                    if aux.getNodoIzda() != None:
                        aux = aux.getNodoIzda()
                    else:
                        aux.insertarIzda(nodo)
                        break
                else:
                    if aux.getNodoDcha() != None:
                        aux = aux.getNodoDcha()
                    else:
                        aux.insertarDcha(nodo)
                        break

    def buscarInformado(self, numero):
        if self._raiz == None:
            return None
        else:
            aux = self._raiz
            while True:
                if (numero < aux.getValor()):
                    if aux.getNodoIzda() != None:
                        aux = aux.getNodoIzda() # Avanza en el árbol
                    else:
                        return None

                elif (numero > aux.getValor()):
                    if aux.getNodoDcha() != None:
                        aux = aux.getNodoDcha() # Avanza en el árbol
                    else:
                        return None
                else:
                    return aux
                    # Si lo encuentra, devolvemos el nodo denominado aux

    def getRaiz(self):
        return self._raiz

    def profundidad(self, nodo):
        if nodo == None:
            return 0
        else:
            return 1 + max(self.profundidad(nodo.getNodoIzda()), self.profundidad(nodo.getNodoDcha()))

    def calculaprofundidad(self):
        return str(self.profundidad(self.getRaiz()))

    def preorden(self, nodo):
        if nodo == None:
            return ""
        print(nodo, end=" ")
        self.preorden(nodo.getNodoIzda())
        self.preorden(nodo.getNodoDcha())

    def recorridopreorden(self):
        self.preorden(self.getRaiz())

    def inorden(self, nodo):
        if nodo == None:
            return ""
        self.inorden(nodo.getNodoIzda())
        print(nodo, end=" ")
        self.inorden(nodo.getNodoDcha())

    def recorridoinorden(self):
        self.inorden(self.getRaiz())

    def posorden(self, nodo):
        if nodo == None:
            return ""
        self.posorden(nodo.getNodoIzda())
        self.posorden(nodo.getNodoDcha())
        print(nodo, end=" ")

    def recorridoposorden(self):
            self.posorden(self.getRaiz())

    def anchura(self, nodo):
        cola = Queue()
        cola.put(nodo)
        while not cola.empty():
            num = cola.get()
            print(num, end=" ")
            if num.getNodoIzda() != None:
                cola.put(num.getNodoIzda())
            if num.getNodoDcha() != None:
                cola.put(num.getNodoDcha())

    def recorridoanchura(self):
        self.anchura(self.getRaiz())

