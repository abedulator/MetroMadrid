import unittest
from main import *
nodo1 = nodo("n1",["n2"])
nodo2 = nodo("n2",["n3","n4","n1"])
nodo3 = nodo("n3",["n2","n5"])
nodo4 = nodo("n4",["n2","n5"])
nodo5 = nodo("n5",["n3","n4"])
grafo_prueba = [nodo1,nodo2,nodo3,nodo4,nodo5]
"""
       Test Graph                               1 -- 2 -- 3
                                                     |    |
                                                     4 -- 5    
"""




class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1+1, 2)

    def test_1(self):
        self.assertEqual(grafo.IsConected(grafo_prueba[0],grafo_prueba[1]),True)


    #def test_2(self):
     #   self.assertEqual(grafo.IsConected(grafo_prueba[2],grafo_prueba[0]),False)

    #  def test_Bonus_Content (self):
    #     self.assertEqual(grafo.camlong(grafo_prueba[0],grafo_prueba[4]),3)
    def test_2(self):
        self.assertEqual(grafo.name2node("n2",grafo_prueba),nodo2)

    def test_fin(self):
        self.assertEqual(grafo.metro(grafo_prueba)[1],5)


if __name__ == '__main__':
    unittest.main()
