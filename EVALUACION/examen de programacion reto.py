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
        # TODO 1: Agregar el nuevo nodo al final de la lista enlazada
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: Agregar un elemento a la cima de la pila
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: Retirar y devolver el elemento de la cima, si existe
        if not self.items:
            return None
        return self.items.pop()

    def cima(self):
        # Reto del caso 31: consultar la cima sin retirar el elemento
        if not self.items:
            return None
        return self.items[-1]


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: Agregar un elemento al final de la cola
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: Retirar y devolver el primer elemento, si existe
        if not self.items:
            return None
        return self.items.pop(0)


if __name__ == "__main__":
    print("=== CASO 31: EQUIPO DE DESARROLLO ===")

    print("\nLista enlazada de solicitudes:")
    solicitudes = ListaEnlazada()
    solicitudes.agregar("DEV01", "Corregir error")
    solicitudes.agregar("DEV02", "Probar")
    solicitudes.agregar("DEV03", "Documentar")
    solicitudes.mostrar()

    print("\nPrueba de la pila:")
    pila = Pila()
    pila.apilar(("DEV01", "Corregir error"))
    pila.apilar(("DEV02", "Probar"))
    pila.apilar(("DEV03", "Documentar"))

    print("Cima antes de consultar:", pila.cima())
    print("Cima consultada:", pila.cima())
    print("Cima después de consultar:", pila.cima())
    print("Cantidad de elementos en la pila:", len(pila.items))

    print("\nPrueba de la cola:")
    cola = Cola()
    cola.encolar(("DEV01", "Corregir error"))
    cola.encolar(("DEV02", "Probar"))
    cola.encolar(("DEV03", "Documentar"))
    print("Sale de la cola:", cola.desencolar())
    print("Elementos restantes en la cola:", cola.items)
