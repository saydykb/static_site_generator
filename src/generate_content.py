import os
from src.markdown_to_nodes import markdown_to_nodes
from src.extract_title import extract_title

def generate_content(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as file:
        markdown = file.read()

    with open(template_path) as file:
        template = file.read()

    node = markdown_to_nodes(markdown)
    content = node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as file:
        file.write(template)
