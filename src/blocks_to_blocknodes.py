import re
from src.htmlnode import HTMLNode
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.block_to_block_type import block_to_block_type, BlockType

def blocks_to_blocknodes(blocks: list[str]) -> list[ParentNode | LeafNode]:
    blocknodes = []

    for block in blocks:

        block_type: BlockType = block_to_block_type(block)

        match block_type:

            case BlockType.HEADING:
                match = re.match(r"^(#{1,6}) ([\s\S]*)", block)
                if match:
                    h_num = len(match[1])
                    node = LeafNode(f"h{h_num}", match[2])
                    blocknodes.append(node)
                else:
                    raise ValueError("Heading block doesn't match regex for heading in markdown_to_html_node")

            case BlockType.CODE:
                match = re.match(r"^```\n([\s\S]*)```", block)
                if match:
                    node = ParentNode("pre", [LeafNode("code", match[1])])
                    blocknodes.append(node)
                else:
                    raise ValueError("Code block doesn't match regex for code in markdown_to_html_node")

            case BlockType.O_LIST:
                lines_html: list[LeafNode] = []
                lines_str: list[str] = block.splitlines()
                for line in lines_str:
                    match = re.match(r"\d+. ([\s\S]*)", line)
                    if match:
                        lines_html.append(LeafNode("li", match[1]))
                    else:
                        raise ValueError("O_list block doesn't match regex for o_list in markdown_to_html_node")
                node = ParentNode(tag="ol",
                                children=lines_html,
                                )
                blocknodes.append(node)

            case BlockType.U_LIST:
                lines_html: list[LeafNode] = []
                lines_str: list[str] = block.splitlines()
                for line in lines_str:
                    match = re.match(r"- ([\s\S]*)", line)
                    if match:
                        lines_html.append(LeafNode("li", match[1]))
                    else:
                        raise ValueError("U_list block doesn't match regex for u_list in markdown_to_html_node")
                node = ParentNode(tag="ul",
                                children=lines_html
                                )
                blocknodes.append(node)

            case BlockType.QUOTE:
                quote: str = ""
                lines_str: list[str] = block.splitlines()
                for line in lines_str:
                    match = re.match(r"> ?([\s\S]*)", line)
                    if match:
                        new_line: str = match[1].strip()
                        quote = quote + new_line + " "
                    else:
                        raise ValueError("Quote block doesn't match regex for quote in markdown_to_html_node")
                node = LeafNode(tag = "blockquote",
                                value = quote,
                                )
                blocknodes.append(node)

            case _: #BlockType.PARAGRAPH
                node = LeafNode(tag = "p",
                                value = block,
                                )
                blocknodes.append(node)

    return blocknodes
