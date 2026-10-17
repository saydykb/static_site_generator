def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)-1, -1, -1):
        blocks[i] = blocks[i].strip()

        if blocks[i] == '':
            blocks.pop(i)
    return blocks
