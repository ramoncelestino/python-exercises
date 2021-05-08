import unittest

import removeVowelsString

class removetests(unittest.TestCase):

    def test_remove(self):
        s = "parabens"
        self.assertEqual(removeVowelsString.removeVowels(s), 'prbns')
        self.assertEqual(removeVowelsString.removeVowels('testes'), 'tsts')

if __name__ == '__main__':
    unittest.main()