import unittest

from translator import englishToFrench, frenchToEnglish

class TestNull(unittest.TestCase):
    def notnullf2e(self):
        self.assertIsNotNone(frenchToEnglish())