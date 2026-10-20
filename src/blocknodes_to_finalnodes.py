from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode
from text_to_textnodes import text_to_textnodes
from textnodes_to_leafnodes import textnodes_to_leafnodes

def blocknodes_to_finalnodes(blocknodes: list[ParentNode | LeafNode]) -> list[ParentNode | LeafNode]:
    finalnodes = []

    for node in blocknodes:
        if isinstance(node, ParentNode):
            new_children = blocknodes_to_finalnodes(node.children)
            new_node = ParentNode(node.tag, new_children)
            finalnodes.append(new_node)

        else:
            
            new_node = node

            if node.value is None:
                raise ValueError("blocknodes that are leafnodes must have a value")

            if node.tag != "code":
                textnodes: list[TextNode] = text_to_textnodes(node.value)
                leafnodes: list[LeafNode] = textnodes_to_leafnodes(textnodes)
                new_node = ParentNode(node.tag, leafnodes)
            
            finalnodes.append(new_node)

    return finalnodes
