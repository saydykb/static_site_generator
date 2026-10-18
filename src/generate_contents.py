import os

from src.generate_content import generate_content

def generate_contents(source_dir_path: str, template_path: str, dest_dir_path: str):

    if not os.path.exists(source_dir_path):
        raise ValueError("source directory path does not exist")
    if not os.path.exists(dest_dir_path):
        raise ValueError("destination directory path does not exist")

    list_dir = os.listdir(source_dir_path)

    for path in list_dir:

        source_path = os.path.join(source_dir_path, path)
        dest_path = os.path.join(dest_dir_path, path)


        is_file = os.path.isfile(source_path)
        is_dir = os.path.isdir(source_path)
        is_markdown = False
        is_html = False

        if len(source_path) >= 5:
            is_markdown = source_path[-3:] == ".md"
            is_html = source_path[-5:] == ".html"
        elif len(source_path) >= 3:
            is_markdown = source_path[-3:] == ".md"
        else:
            raise ValueError(f"{source_path} is to short to be valid")

        if is_file and is_markdown: 
            dest_path = dest_path[0:-3] + ".html"
            generate_content(source_path, template_path, dest_path)

        elif is_file and is_html:
            generate_content(source_path, template_path, dest_path)

        elif os.path.isdir(source_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_contents(source_path, template_path, dest_path)
        
        else:
            raise ValueError(f"{source_path} is not a file or a directory")


            


