import unittest
from src.textnode import TextNode, TextType
from src.split_nodes_link import extract_markdown_links, split_nodes_link

class TestExtractMarkdownLinks(unittest.TestCase):
    def setUp(self):
        self.text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.text_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.text_both = self.text_link + " " + self.text_image

    def test_extract_markdown_links(self):
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extract_markdown_links(self.text_link))

    def test_extract_markdown_both(self):
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extract_markdown_links(self.text_both))

class TestSplitNodesLink(unittest.TestCase):

    def test_split_link(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT)

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ],
        new_nodes,
    )
