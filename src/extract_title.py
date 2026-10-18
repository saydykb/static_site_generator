import re

def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()
    for line in lines:
        match = re.fullmatch(r"^# ?(.*)", line)
        if match:
            return match[1].strip()
    raise ValueError("There is no #Header in the markdown")



