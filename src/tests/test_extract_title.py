import unittest
from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def setUp(self):
        self.header1 = '''#This is a Header   '''
        self.header2 = '''# This is also a valid header'''
        self.header3 = r'''# This has a valid header
but also other text
yay'''
        self.header4 = r''' this has text # but is not a header'''
        self.header5 = '''This is not a valid header'''

    def test_extract_title(self):
        self.assertEqual(extract_title(self.header1), "This is a Header")
        self.assertEqual(extract_title(self.header2), "This is also a valid header")
        self.assertEqual(extract_title(self.header3), "This has a valid header")
        with self.assertRaises(ValueError):
            extract_title(self.header4)
            extract_title(self.header5)
        
