import unittest
from main import *
nodo1 = nodo("n1",["n2"])
nodo2 = nodo("n2",["n3","n4"])
nodo3 = nodo("n3",["n2","n5"])
nodo4 = nodo("n4",["n2","n5"])
nodo5 = nodo("n5",["n3","n4"])
grafo_prueba = grafo([nodo1,nodo2,nodo3,nodo4,nodo5])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1+1, 2)

    def test_1(self):
        self.assertEqual(grafo.metrolong(grafo_prueba),5)


if __name__ == '__main__':
    unittest.main()
