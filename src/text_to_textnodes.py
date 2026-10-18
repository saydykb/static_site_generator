from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from src.split_nodes_delimiter import split_nodes_delimiter
from src.split_nodes_image import split_nodes_image
from src.split_nodes_link import split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
