from unittest import TestCase
from src.split_nodes_delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodesDelimiter(TestCase):
    maxDiff=None
    def setUp(self):
    # Text Nodes that work
        self.text_node_no_markdown = TextNode("This is a string without markdown in it", TextType.TEXT)
        self.text_node_bold = TextNode("This is a string with **bold text**. Even though some **text** may not **need to **be bolded.", TextType.TEXT)
        self.text_node_italic = TextNode("This is a _string_ without _much_ expression. It uses _italics._", TextType.TEXT)
        self.text_node_code = TextNode("This is a `code` string. In `both meanings of` the word.", TextType.TEXT)
    # Text Nodes with markdown mistakes
        self.text_node_bold_no_close = TextNode("This is a **bold** string with **bad markdown.", TextType.TEXT)
        self.text_node_italic_no_close = TextNode("This is a _italic string with _bad_ markdown.", TextType.TEXT)
        self.text_node_code_no_close = TextNode("This is a `code string with ` bad `markdown.", TextType.TEXT)
    # Text Node Lists
        self.node_list_working = [self.text_node_no_markdown, self.text_node_bold, self.text_node_italic, self.text_node_code]
        self.node_list_all = self.node_list_working.copy() + [self.text_node_bold_no_close, self.text_node_italic_no_close, self.text_node_code_no_close]

    def test_split_node_delimiter_bold(self):
        self.assertEqual(split_nodes_delimiter([self.text_node_bold], "**", TextType.BOLD),
                         [
                             TextNode("This is a string with ", TextType.TEXT),
                              TextNode("bold text", TextType.BOLD),
                              TextNode(". Even though some ", TextType.TEXT),
                              TextNode("text", TextType.BOLD),
                              TextNode(" may not ", TextType.TEXT),
                              TextNode("need to ", TextType.BOLD),
                              TextNode("be bolded.", TextType.TEXT),
                            ]
                         )

    def test_split_node_delimiter_italic(self):
        self.assertEqual(split_nodes_delimiter([self.text_node_italic], "_", TextType.ITALIC), 
                         [
                             TextNode("This is a ", TextType.TEXT),
                             TextNode("string", TextType.ITALIC),
                             TextNode(" without ", TextType.TEXT),
                             TextNode("much", TextType.ITALIC),
                             TextNode(" expression. It uses ", TextType.TEXT),
                             TextNode("italics.", TextType.ITALIC),
                            ]
                         )

    def test_split_node_delimiter_code(self):
        self.assertEqual(split_nodes_delimiter([self.text_node_code], "`", TextType.CODE),
                         [
                             TextNode("This is a ", TextType.TEXT),
                             TextNode("code", TextType.CODE),
                             TextNode(" string. In ", TextType.TEXT),
                             TextNode("both meanings of", TextType.CODE),
                             TextNode(" the word.", TextType.TEXT),
                            ]
                         )

    def test_split_node_delimiter_exceptions(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter([self.text_node_bold_no_close], "**", TextType.BOLD)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([self.text_node_italic_no_close], "_", TextType.ITALIC)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([self.text_node_code_no_close], "`", TextType.CODE)

    def test_split_node_delimiter_all(self):
        self.assertEqual(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(self.node_list_working, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE),
                         [
                             TextNode("This is a string without markdown in it", TextType.TEXT),
                             TextNode("This is a string with ", TextType.TEXT),
                             TextNode("bold text", TextType.BOLD),
                             TextNode(". Even though some ", TextType.TEXT),
                             TextNode("text", TextType.BOLD),
                             TextNode(" may not ", TextType.TEXT),
                             TextNode("need to ", TextType.BOLD),
                             TextNode("be bolded.", TextType.TEXT),
                             TextNode("This is a ", TextType.TEXT),
                             TextNode("string", TextType.ITALIC),
                             TextNode(" without ", TextType.TEXT),
                             TextNode("much", TextType.ITALIC),
                             TextNode(" expression. It uses ", TextType.TEXT),
                             TextNode("italics.", TextType.ITALIC),
                             TextNode("This is a ", TextType.TEXT),
                             TextNode("code", TextType.CODE),
                             TextNode(" string. In ", TextType.TEXT),
                             TextNode("both meanings of", TextType.CODE),
                             TextNode(" the word.", TextType.TEXT),
                            ]
                         )

    def test_split_node_delimiter_all_error(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(self.node_list_all, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
