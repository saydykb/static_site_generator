from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def block_to_block_type(text: str) -> BlockType:
    if re.fullmatch(r"#{1,6} [\s\S]*", text):
        return BlockType.HEADING
    elif re.fullmatch(r"`{3}\n[\s\S]*`{3}", text):
        return BlockType.CODE
    elif re.fullmatch(r"(?:>.*\n?)+", text):
        return BlockType.QUOTE
    elif re.fullmatch(r"(?:- .*\n?)+", text):
        return BlockType.U_LIST
    elif is_o_list(text):
         return BlockType.O_LIST
    else:
        return BlockType.PARAGRAPH

def is_o_list(text: str) -> bool:
    lines = text.splitlines()
    i = 1
    for line in lines:
        if not re.fullmatch(r"^\d+\. .*", line):
            return False
        if line[0] != str(i):
            return False
        i += 1
    return True


