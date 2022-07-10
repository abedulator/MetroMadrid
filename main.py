class nodo:
    def __init__(self,nombre,conexiones,factible = False):
        self.nombre = nombre
        self.conexiones = conexiones
        self.factible = factible

class grafo:
    def IsConected(nodo1,nodo2):
        return nodo2.nombre in nodo1.conexiones

    """    def camlong(self,nodo1,nodo2):
        longi = 1
        visited = []
        if not self.IsConected(nodo1,nodo2):
            ++longi
            for e in nodo1.conexiones:
                if not self.IsConected(e,nodo2):
                    visited.append(e)

                else:
                    return longi




        return longi
    """
    def minimetrolong(nodos,visited,long):
        pass
        # return [visited,long]

    def metrolong(nodos,start = []):
        pass
        #

