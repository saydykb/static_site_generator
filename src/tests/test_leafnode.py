from unittest import TestCase 
from src.leafnode import LeafNode

class TestLeafNode(TestCase):
    def setUp(self):
        self.node1 = LeafNode('a', "This is a link.", {"href": "https://www.google.com", "id": "link"})
        self.node2 = LeafNode("p", "Hello, world!")
        self.node3 = LeafNode(None, "This is plain text.")
        self.node4 = LeafNode(None, "This is also plain text, but with props.", {"id": "not_a_link"})

    def test_leaf_to_html_no_tag(self):
        self.assertEqual(self.node3.to_html(), "This is plain text.")

    def test_leaf_to_html_no_tag_props(self):
        self.assertEqual(self.node4.to_html(), "This is also plain text, but with props.")

    def test_leaf_to_html_p(self):
        self.assertEqual(self.node2.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link_tags(self):
        self.assertEqual(self.node1.to_html(), "<a href=https://www.google.com id=link>This is a link.</a>")

    def test_repr(self):
        self.assertEqual(repr(self.node1), "LeafNode(tag: a, value: This is a link., props: {'href': 'https://www.google.com', 'id': 'link'})")

