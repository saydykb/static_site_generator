import os
from src.generate_files import generate_files
from src.generate_content import generate_content

def main():
    generate_files("static", "public")
    generate_content("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
