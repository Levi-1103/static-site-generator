from inline_markdown import extract_markdown_images, split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



def main():

    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
    new_nodes = split_nodes_image([node])
    
    print(new_nodes)
if __name__ == "__main__":
    main()
