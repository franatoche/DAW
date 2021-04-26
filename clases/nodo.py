# Clase Nodo
class Nodo(object):

    def __init__(self, valor=None):
        self._valor = valor
        self._padre = None
        self._hijoizda = None
        self._hijodcha = None

    def insertarInformado(self, nodo):
        if nodo._valor <= self._valor:
            self.insertarIzda(nodo)
        else:
            self.insertarDcha(nodo)
        nodo.setPadre(self)

    def setPadre(self, nodo):
        self._padre = nodo

    def getNodoIzda(self):
        return self._hijoizda

    def getNodoDcha(self):
        return self._hijodcha

    def getPadre(self):
        return self._padre

    def insertarDcha(self, nodo):
        self._hijodcha = nodo
        nodo.setPadre(self)

    def insertarIzda(self, nodo):
        self._hijoizda = nodo
        nodo.setPadre(self)

    def podarhijoDcha(self):
        aux = self._hijodcha
        self._hijodcha._padre = None
        self._hijodcha = None
        return aux

    def podarhijoIzda(self):
        aux = self._hijoizda
        self._hijoizda._padre = None
        self._hijoizda = None
        return aux


    def getValor(self):
        return self._valor

    def setValor(self, valor):
        self._valor = valor

    def __str__(self):
        return str(self._valor)
