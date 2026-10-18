import re
from .textnode import TextNode, TextType

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.type is TextType.TEXT:
            remaining_text: str = node.text
            markdown_images: list[tuple[str, str]] = extract_markdown_images(node.text)
            for image in markdown_images:
                split_text: list[str] = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                remaining_text =  split_text[1]
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if remaining_text != '':
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
