import os
from src.generate_files import generate_files
from src.generate_content import generate_content

def main():
    generate_files("static", "public")
    generate_content("content/index.md", "template.html", "public/index.html")
    generate_content("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_content("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_content("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_content("content/contact/index.md", "template.html", "public/contact/index.html")

if __name__ == "__main__":
    main()
