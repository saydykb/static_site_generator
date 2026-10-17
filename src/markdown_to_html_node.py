import re
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes, TextNode, TextType
from textnode import text_node_to_html_node
from parentnode import ParentNode

def block_to_html_node(block: str) ->HTMLNode:
    type: BlockType = block_to_block_type(block)
    match type:
        case BlockType.HEADING:
            match = re.match(r"^(#{1,6}) ([\s\S]*)", block)
            if match:
                h_num = len(match[0])
                node = HTMLNode(f"h{h_num}", match[1])
                return node
            else:
                raise ValueError("Heading block doesn't match regex for heading in markdown_to_html_node")

        case BlockType.CODE:
            match = re.match(r"^```\n([\s\S]*)'''", block)
            if match:
                node = HTMLNode("code", match[1])
                return node
        case BlockType.O_LIST:
            lines_html: list[HTMLNode] = []
            lines_str: list[str] = block.splitlines()
            for line in lines_str:
                match = re.match(r"\d+. ([\s\S]*)", line)
                if match:
                    lines_html.append(HTMLNode("li", match[0]))
                else:
                    raise ValueError("O_list block doesn't match regex for o_list in markdown_to_html_node")
            node = HTMLNode(tag="ol",
                            value=None,
                            children=lines_html,
                            )
            return node
        case BlockType.U_LIST:
            lines_html: list[HTMLNode] = []
            lines_str: list[str] = block.splitlines()
            for line in lines_str:
                match = re.match(r"- ([\s\S]*)", block)
                if match:
                    lines_html.append(HTMLNode("li", match[0]))
                else:
                    raise ValueError("U_list block doesn't match regex for u_list in markdown_to_html_node")
            node = HTMLNode(tag="ul",
                            value=None,
                            children=lines_html
                            )
            return node
        case BlockType.QUOTE:
            quote: str = ""
            lines_str: list[str] = block.splitlines()
            for line in lines_str:
                match = re.match(r"> ?([\s\S]*)", block)
                if match:
                    new_line: str = match[0].strip()
                    quote = quote + new_line + " "
                else:
                    raise ValueError("Quote block doesn't match regex for quote in markdown_to_html_node")
            node = HTMLNode(tag = "blockquote",
                            value = quote,
                            children = None
                            )
            return node
        case _:
            node = HTMLNode(tag = "p",
                            value = block,
                            children = None,
                            )
            return node

def html_node_to_parent_node(node: HTMLNode) -> ParentNode:
    text_nodes: list[TextNode] = text_to_textnodes(node.value)
    html_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return ParentNode(node.tag, html_nodes)

def markdwon_to_html_node(markdown: str) -> HTMLNode:
    main_node = ParentNode("div", [])
    blocks: list[str] = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = block_to_html_node(block)
        parent_node = html_node_to_parent_node(html_node)
        main_node.children.append(parent_node)
    return main_node




