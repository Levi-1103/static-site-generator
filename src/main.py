from markdown_blocks import markdown_to_blocks, markdown_to_html_node
from inline_markdown import (
    extract_markdown_images,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():

    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    print(markdown_to_html_node(markdown))


if __name__ == "__main__":
    main()
