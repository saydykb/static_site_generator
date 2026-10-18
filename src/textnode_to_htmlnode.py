from .textnode import TextNode
from .textnode import TextType
from .leafnode import LeafNode


def textnode_to_htmlnode(text_node: TextNode) -> LeafNode:
    if text_node.type not in TextType:
        raise Exception("not a valid text type")
    match text_node.type:

        case TextType.TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode("b", text_node.text)

        case TextType.ITALIC:
            return LeafNode("i", text_node.text)

        case TextType.CODE:
            return LeafNode("code", text_node.text)

        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
