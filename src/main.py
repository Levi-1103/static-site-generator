from inline_markdown import split_nodes_delimiter, validate_markdown
from textnode import TextNode
from htmlnode import HTMLNode



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



delimiter_code = "`"
delimiter_bold = "**"
delimiter_italic = "*"


def main():
    
    node = TextNode("This is text with a **code block** word", text_type_text)

    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

    print(new_nodes)


if __name__ == "__main__":
    main()
