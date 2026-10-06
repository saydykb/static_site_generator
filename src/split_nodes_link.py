import re
from textnode import TextNode, TextType

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.type is TextType.TEXT:
            remaining_text: str = node.text
            markdown_links: list[tuple[str, str]] = extract_markdown_links(node.text)
            for link in markdown_links:
                split_text: list[str] = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                remaining_text = split_text[1]
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if remaining_text != '':
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes






