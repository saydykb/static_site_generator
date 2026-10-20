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
