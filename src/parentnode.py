from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, 
                 tag: str | None,
                 children: list[HTMLNode],
                 props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag must have a value")
        if not self.children:
            raise ValueError("the ParentNode must have children")
        children_html = ''
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag + self.props_to_html()}>{children_html}</{self.tag}>"

    
