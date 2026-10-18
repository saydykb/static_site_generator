from src.htmlnode import HTMLNode
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.textnode import TextNode
from src.text_to_textnodes import text_to_textnodes
from src.textnodes_to_leafnodes import textnodes_to_leafnodes

def blocknodes_to_finalnodes(node: ParentNode | LeafNode) -> ParentNode | LeafNode:

    if node is ParentNode:
        children = []

        for child in node.children:
            children.append(blocknodes_to_finalnodes(child))

        node.children = children

        return node

    new_node = node

    if node.value is None:
        raise ValueError("blocknodes that are leafnodes must have a value")

    if node.tag != "code":
        textnodes: list[TextNode] = text_to_textnodes(node.value)
        leafnodes: list[LeafNode] = textnodes_to_leafnodes(textnodes)
        new_node = ParentNode(node.tag, leafnodes)

    return new_node
            
