import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is a text node"})

if __name__ == "__main__":
    unittest.main()
