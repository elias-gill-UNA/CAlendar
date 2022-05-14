import unittest
from ..integracion_web import test

class TesteoDb(unittest.TestCase):
    def testCargar(self):
        self.assertEqual(test(),1,"Debe de retornar 1")

if __name__ == '__main__':
    unittest.main()
