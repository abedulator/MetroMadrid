class nodo:
    def __init__(self,nombre,conexiones,factible = False):
        self.nombre = nombre
        self.conexiones = conexiones
        self.factible = factible

class grafo:
    def __init__(self,nodos,inicio = False):
        self.nodos = nodos
        self.inicio = inicio

    def metrolong(self):
        pass

    def metrocamino(self):
        pass

