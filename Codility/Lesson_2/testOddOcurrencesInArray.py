import OddOcurrencesInArray
import unittest

class testOddOcurrencesInArray(unittest.TestCase):

    def test_multiples(self):
        self.assertEqual(OddOcurrencesInArray.solution([1,2,1,2,3,3,4,4,1,4,1]), 3)