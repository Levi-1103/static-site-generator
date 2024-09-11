import unittest

from inlinenode import split_nodes_delimiter
from textnode import TextNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TestInlineNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
        )
    
    def test_split_nodes_delimiter_missing_delimeter(self):
        node = TextNode("This is text with a `code block word", text_type_text)

        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        
    