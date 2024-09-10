from textnode import TextNode
from htmlnode import HTMLNode


def main():
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")

    htmlNode = HTMLNode(
        "p",
        "This is a html tag",
        None,
        {
            "href": "https://www.google.com",
            "target": "_blank",
        },
    )

    print(htmlNode)


if __name__ == "__main__":
    main()
