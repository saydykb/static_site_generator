from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from leafnode import LeafNode
from blocks_to_blocknodes import blocks_to_blocknodes
from blocknodes_to_finalnodes import blocknodes_to_finalnodes

def markdown_to_nodes(markdown: str) -> ParentNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    blocknodes: list[ParentNode | LeafNode] = blocks_to_blocknodes(blocks)
    finalnodes = blocknodes_to_finalnodes(blocknodes)
    return ParentNode("div", finalnodes)
