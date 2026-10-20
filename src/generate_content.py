import os
import sys
from markdown_to_nodes import markdown_to_nodes
from extract_title import extract_title

def generate_content(source_path: str, template_path: str, dest_path: str):
    if not os.path.exists(source_path):
        raise ValueError(f"{source_path} does not exist")
    if not os.path.isfile(source_path):
        raise ValueError(f"{source_path} is not a file")

    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    print(f"Generating page from {source_path} to {dest_path} using {template_path}.")

    with open(source_path) as file:
        markdown = file.read()

    with open(template_path) as file:
        template = file.read()
    
    node = markdown_to_nodes(markdown)
    content = node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as file:
        file.write(template)
