class HTMLNode:
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None,
                 ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self)-> str:
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ''
        if self.props is not None:
            for prop in self.props:
                html_string += f' {prop}={self.props[prop]}'
        return html_string
    
    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}'
