import unittest
from main import *
grafo_prueba = {
    1 : [2],
    2: [3,4],
    3: [2,5],
    4: [2,5],
    5: [3,4]
}

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1+1, 2)

    def test_1(self):
        self.assertEqual(Lmao.metrolong(grafo_prueba,1),5)


if __name__ == '__main__':
    unittest.main()
