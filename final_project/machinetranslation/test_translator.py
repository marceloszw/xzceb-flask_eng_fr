import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", "French to English translation failed.")
        
    def test2(self):
        self.assertNotEqual(french_to_english(" "), None, "French to English Null Input Error")

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", "English to French translation failed.")
        
    def test2(self):
        self.assertNotEqual(english_to_french(" "), None, "English to French Null Input Error")

unittest.main()