from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, type: TextType, url: str | None = None) -> None:
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other) -> bool:
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.type.value}, {self.url})"



def text_node_to_html_node(text_node: TextNode) -> LeafNode:
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
