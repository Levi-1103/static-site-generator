class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html_props = ""
        if self.props is None:
            return html_props

        for attribute in self.props:
            html_props += f' {attribute}="{self.props[attribute]}"'

        return html_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML missing tag")
        if not self.children:
            raise ValueError("Missing children")

        # open tags
        props_str = ""
        if self.props is None:
            props_str = ""
        else:
            props_str = self.props.props_to_html()

        tags = f"<{self.tag}{props_str}>"

        for child in self.children:
            tags += child.to_html()
        # close tags
        tags += f"</{self.tag}>"

        return tags

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.props}, {self.children})"