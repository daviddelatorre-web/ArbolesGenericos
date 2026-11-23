class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.hijoIzquierdo = None
        self.hijoDerecho = None

class ArbolBinario:
    def __init__(self, clave):
        self.raiz = None
        self.clave = clave

    def insertarNodo(self, dato):
        self.raiz = self._insertar(self.raiz, dato)
    def _insertar(self, actual, dato):
        if actual is None:
            return NodoArbol(dato)
        if self.clave(dato) < self.clave(actual.dato):
            actual.hijoIzquierdo = self._insertar(actual.hijoIzquierdo, dato)
        elif self.clave(dato) > self.clave(actual.dato):
            actual.hijoDerecho = self._insertar(actual.hijoDerecho, dato)
        return actual
    def buscarNodo(self, dato):
        return self._buscar(self.raiz, self.clave(dato))
    def _buscar(self, actual, clave):
        if actual is None:
            return False
        if self.clave(actual.dato) == clave:
            return True
        if clave < self.clave(actual.dato):
            return self._buscar(actual.hijoIzquierdo, clave)
        return self._buscar(actual.hijoDerecho, clave)
    def eliminarNodo(self, dato):
        self.raiz = self._eliminar(self.raiz, self.clave(dato))
    def _eliminar(self, actual, clave):
        if actual is None:
            return None
        if clave < self.clave(actual.dato):
            actual.hijoIzquierdo = self._eliminar(actual.hijoIzquierdo, clave)
        elif clave > self.clave(actual.dato):
            actual.hijoDerecho = self._eliminar(actual.hijoDerecho, clave)
        else:
            if actual.hijoIzquierdo is None and actual.hijoDerecho is None:
                return None
            elif actual.hijoIzquierdo is None:
                return actual.hijoDerecho
            elif actual.hijoDerecho is None:
                return actual.hijoIzquierdo
            else:
                sucesor = self._minimo(actual.hijoDerecho)
                actual.dato = sucesor.dato
                actual.hijoDerecho = self._eliminar(actual.hijoDerecho, self.clave(sucesor.dato))
        return actual
    def _minimo(self, actual):
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual
    def inOrden(self):
        self._inOrden(self.raiz)
        print()
    def _inOrden(self, actual):
        if actual is not None:
            self._inOrden(actual.hijoIzquierdo)
            print(actual.dato)
            self._inOrden(actual.hijoDerecho)
    def preOrden(self):
        self._preOrden(self.raiz)
        print()
    def _preOrden(self, actual):
        if actual is not None:
            print(actual.dato)
            self._preOrden(actual.hijoIzquierdo)
            self._preOrden(actual.hijoDerecho)
    def postOrden(self):
        self._postOrden(self.raiz)
        print()
    def _postOrden(self, actual):
        if actual is not None:
            self._postOrden(actual.hijoIzquierdo)
            self._postOrden(actual.hijoDerecho)
            print(actual.dato)
    def imprimirArbol(self):
        self._imprimirArbol(self.raiz, 0)
    def _imprimirArbol(self, actual, nivel):
        if actual is not None:
            self._imprimirArbol(actual.hijoDerecho, nivel + 1)
            print("    " * nivel + str(actual.dato))
            self._imprimirArbol(actual.hijoIzquierdo, nivel + 1)