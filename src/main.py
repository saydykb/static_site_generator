import os
from src.generate_files import generate_files
from src.generate_contents import generate_contents

def main():
    generate_files("static", "public")
    generate_contents("content", "template.html", "public")

if __name__ == "__main__":
    main()
