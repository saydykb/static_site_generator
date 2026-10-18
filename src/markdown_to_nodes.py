from src.markdown_to_blocks import markdown_to_blocks
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.blocks_to_blocknodes import blocks_to_blocknodes
from src.blocknodes_to_finalnodes import blocknodes_to_finalnodes

def markdown_to_nodes(markdown: str) -> ParentNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    blocknodes: list[ParentNode | LeafNode] = blocks_to_blocknodes(blocks)
    finalnodes = blocknodes_to_finalnodes(blocknodes)
    return ParentNode("div", finalnodes)
