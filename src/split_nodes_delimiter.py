from .textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: TextType
                          ) -> list[TextNode]:

    split_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.type is TextType.TEXT:
            text_split = node.text.split(delimiter)
            if len(text_split) % 2 != 1:
                raise ValueError(f"Invalid markdown syntax. Must have closing '{delimiter}'.")
            for i in range(len(text_split)):
                if text_split[i] != "":
                    if i % 2 == 0:
                        split_nodes.append(TextNode(text_split[i], TextType.TEXT))
                    else:
                        split_nodes.append(TextNode(text_split[i], text_type))
        else:
            split_nodes.append(node)
    return split_nodes

