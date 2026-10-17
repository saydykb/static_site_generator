import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def setUp(self):
        self.paragraph_str = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        self.heading_str = "# This is a heading"
        self.code_str = "```\nblock_to_block.py\ncoding here```"
        self.quote_str = """>An apple a day.
> Keeps the doctor away"""
        self.u_list_str = '''- This is the first list item in a list block
- This is a list item
- This is another list item'''
        self.o_list_str = """1. task 1
2. task 3
3. task 4"""
        self.not_o_list_str = """1. task 1
3. task 4
3. another task"""

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type(self.paragraph_str), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type(self.heading_str), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type(self.code_str), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type(self.quote_str), BlockType.QUOTE)

    def test_block_to_block_type_u_list(self):
        self.assertEqual(block_to_block_type(self.u_list_str), BlockType.U_LIST)

    def test_block_to_block_type_o_list(self):
        self.assertEqual(block_to_block_type(self.o_list_str), BlockType.O_LIST)
        self.assertNotEqual(block_to_block_type(self.not_o_list_str), BlockType.O_LIST)
