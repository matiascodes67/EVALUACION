class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1...
        pass

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2
        pass

    def desapilar(self):
        # TODO 3 ...
        pass

    def cima(self):
        # Caso 31: consultar la cima sin retirarla
        if not self.items:
            return None
        return self.items[-1]

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4
        pass

    def desencolar(self):
        # TODO 5 ...
        pass
