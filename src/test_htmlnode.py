import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node1 = HTMLNode('p', "this is paragraph text", props={"href": "https://google.com", "target": "_blank",})

    def test_props_to_html(self):
        self.assertEqual(self.node1.props_to_html(), " href=https://google.com target=_blank")

    def test_repr(self):
        self.assertEqual(repr(self.node1), "HTMLNode(tag: p, value: this is paragraph text, children: None, props: {'href': 'https://google.com', 'target': '_blank'}")

    def test_to_html(self):
        self.assertRaises(NotImplementedError, self.node1.to_html)

