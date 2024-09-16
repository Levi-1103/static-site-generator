from textnode import TextNode,text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    delimiter_code = "`"
    delimiter_bold = "**"
    delimiter_italic = "*"



    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)

        if validate_markdown(node.text, delimiter):
            split_text = node.text.split(delimiter)
            node_type = ""
            if delimiter == delimiter_code:
                node_type = text_type_code
            if delimiter == delimiter_bold:
                node_type = text_type_bold
            if delimiter == delimiter_italic:
                node_type = text_type_italic
            
            isDelimiter = False

            for value in split_text:
                print(value)
                if value == "":
                    continue
                if isDelimiter == False:
                    new_nodes.append(TextNode(value, text_type_text))
                    isDelimiter = True
                else:
                    new_nodes.append(TextNode(value, node_type))
                    isDelimiter = False

    return new_nodes



def validate_markdown(text, delimiter):
    count = 0

    count = text.count(delimiter)

    if count % 2 != 0:
        raise ValueError(f"Invalid markdown: Unclosed {delimiter} delimiter ")
    
    return True



def extract_markdown_images(text):

    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches  = re.findall(pattern, text)

    return matches

def extract_markdown_links(text):

    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    return matches


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            link_alt = link[0]
            link_text = link[1]
            sections = original_text.split(f"[{link_alt}]({link_text})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
        return new_nodes
    


def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        original_text = node.text

        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            image_alt = image[0]
            image_link = image[1]

            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            original_text = sections[1]

        if original_text != "":
                new_nodes.append(TextNode(original_text, text_type_text))
            
        return new_nodes