from inline_markdown import extract_markdown_images, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



def main():

    # text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    node = TextNode("**bold** and *italic*", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)

    print(new_nodes)


    
if __name__ == "__main__":
    main()
