import unittest
from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node_iw = TextNode("This is node1", TextType.ITALIC, "website.com")
        self.node_i = TextNode("This is node1.5", TextType.CODE, "nets.com")
        self.node_i2 = TextNode("This is node1.5", TextType.CODE, "nets.com")
        self.node_bw = TextNode("This is node2", TextType.BOLD, "websting.com")
        self.node_bw2 = TextNode("This is node2", TextType.BOLD, "websting.com")

    def test_eq(self):
        self.assertEqual(self.node_bw, self.node_bw2)

    def test_eq_no_website(self):
        self.assertEqual(self.node_i, self.node_i2)

    def test_text_type(self):
        self.assertEqual(TextType.ITALIC.value, "italic")
        self.assertEqual(TextType.BOLD.value, "bold")
        self.assertEqual(TextType.CODE.value, "code")
        self.assertEqual(TextType.LINK.value, "link")
        self.assertEqual(TextType.IMAGE.value, "image")

    def test_repr(self):
        self.assertEqual(repr(self.node_iw), 'TextNode(This is node1, italic, website.com)')

    def test_repr_no_website(self):
        self.assertEqual(repr(self.node_i), 'TextNode(This is node1.5, code, nets.com)')


if __name__ == "__main__":
    unittest.main()
