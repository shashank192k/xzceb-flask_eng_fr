import unittest
from translator import englishtofrench,frenchtoenglish


class Testtranslator(unittest.TestCase):

    def test_eng2fr(self):
        self.assertEqual(englishtofrench('Bad'),'Mauvais')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench(' '),' ')


    def test_fr2eng(self):
        self.assertEqual(frenchtoenglish('Mauvais'),'Bad')
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish(' '),' ')    

unittest.main()