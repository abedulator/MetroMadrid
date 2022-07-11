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
    def name2node(name,nodos):
        for x in nodos:
            if x.nombre == name:
                return x

    def minimetro(nodos,visited,long,actual_node):
        for nod in actual_node.conexiones:
            if nod in visited:
                continue
            else:
                visited.append(nod)
                ++long
                grafo.minimetro(nodos, visited, long, grafo.name2node(nod,nodos))
        return [visited,long]


    def metro(nodos,start = []):
        maxim = [[],1]
        if start == []:
            list = nodos
        else:
            list = start
        for ele in list:
            val = grafo.minimetro(nodos,[ele.nombre],1,ele)
            if val[1] > maxim[1]:
                maxim = val

        return maxim

