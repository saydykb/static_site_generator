from src.textnode import TextNode, TextType
from src.leafnode import LeafNode


def textnodes_to_leafnodes(textnodes: list[TextNode]) -> list[LeafNode]:
    leafnodes = []
    for textnode in textnodes:
        match textnode.type:
            
            case TextType.BOLD:
                leafnodes.append(LeafNode("b", textnode.text))

            case TextType.ITALIC:
                leafnodes.append(LeafNode("i", textnode.text))

            case TextType.CODE:
                leafnodes.append(LeafNode("code", textnode.text))

            case TextType.LINK:
                leafnodes.append(LeafNode("a", textnode.text, {"href": textnode.url}))

            case TextType.IMAGE:
                leafnodes.append(LeafNode("img", "", {"src": textnode.url, "alt": textnode.text}))

            case TextType.TEXT:
                leafnodes.append(LeafNode("", textnode.text))

    return leafnodes
