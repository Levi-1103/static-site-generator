from textnode import TextNode



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

delimiter_code = "`"
delimiter_bold = "**"
delimiter_italic = "*"

#ADD UNIT TESTS

def split_nodes_delimiter(old_nodes, delimiter, text_type):


    nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            nodes.append(node)

        if validate_markdown(node.text, delimiter):
            split_text = node.text.split(delimiter)

            isCode = False

            for value in split_text:
                if isCode == False:
                    nodes.append(TextNode(value, text_type_text))
                    isCode = True
                else:
                    nodes.append(TextNode(value, text_type_code))
                    isCode = False

    return nodes


#ADD UNIT TESTS


def validate_markdown(text, delimiter):
    count = 0

    count = text.count(delimiter)

    if count % 2 != 0:
        raise ValueError(f"Invalid markdown: Unclosed {delimiter} delimiter ")
    
    return True

