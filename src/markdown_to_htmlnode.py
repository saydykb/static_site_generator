import re

from .htmlnode import HTMLNode
from .text_to_textnodes import text_to_textnodes, TextNode
from .textnode_to_htmlnode import textnode_to_htmlnode
from .parentnode import ParentNode
from .block_to_htmlnode import block_to_htmlnode
from .markdown_to_blocks import markdown_to_blocks
from .htmlnode_to_parentnode import htmlnode_to_parentnode

def markdown_to_htmlnode(markdown: str) -> HTMLNode:
    main_node = ParentNode("div", [])
    blocks: list[str] = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = block_to_htmlnode(block)
        parent_node = htmlnode_to_parentnode(html_node)
        main_node.children.append(parent_node)
    return main_node




