import os
import sys

from generate_files import generate_files
from generate_contents import generate_contents


def main():
    generate_files("static", "docs")
    generate_contents("content", "template.html", "docs")

if __name__ == "__main__":
    main()
