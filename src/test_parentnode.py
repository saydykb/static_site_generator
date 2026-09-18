from unittest import TestCase
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(TestCase):
    maxDiff = None
    def setUp(self):

        #Leaf Nodes (lvl 5)
        self.leafnode1 = LeafNode("a",
                                  "This is a link.",
                                  {"href": "https://www.google.com", "id": "link"}
                                  )
        self.leafnode2 = LeafNode("p",
                                  "Hello, world!"
                                  )
        self.leafnode3 = LeafNode("h1",
                                  "First Header",
                                  {"id": "header_1"}
                                  )
        self.leafnode4 = LeafNode("h2",
                                  "cat_picture",
                                  {"id": "header_2"}
                                  )
        self.leafnode5 = LeafNode("span",
                                  "Some span text.",
                                  {"class": "highlight"}
                                  )
        self.leafnode6 = LeafNode("a",
                                  "Another link.",
                                  {"href": "https://example.com"}
                                  )
        self.leafnode7 = LeafNode("p",
                                  "Another Paragraph.",
                                  {"class": "description"}
                                  )
        self.leafnode8 = LeafNode("span",
                                  "another span text.",
                                  {
                                      "class": "highlight",
                                      "id": "span_2"
                                    }
                                  )
        self.leafnode9 = LeafNode("h1",
                                  "more headers",
                                  {
                                      "class": "header_1",
                                      "id": "header_1_2"
                                    }
                                  )
        self.leafnode10 = LeafNode("p",
                                   "hopefully the last paragraph.",
                                   {
                                       "class": "paragraph",
                                       "id": "paragraph_last?"
                                    },
                                   )
        self.leafnode11 = LeafNode("h6",
                                   "closing header",
                                   )
        #Parent Nodes to test raising errors
        self.parentnode_no_tag = ParentNode(None,
                                            [
                                                self.leafnode1,
                                                self.leafnode2
                                            ],
                                            {
                                                "id": "no_tag"
                                            }
                                            )
        self.parentnode_no_children = ParentNode("p",
                                                 None
                                                 )

        # 5 levels of parent nodes (lvl 5 is the leaf nodes)
        # Parent Nodes with Leaf Children (lvl 4)
        self.parentnode_4_1 = ParentNode("p",
                                      [
                                          self.leafnode1,
                                          self.leafnode2
                                        ],
                                      {
                                          "id": "parent_node_4_1"
                                        }
                                      )
        self.parentnode_4_2 = ParentNode("div",
                                      [
                                          self.leafnode3,
                                          self.leafnode4
                                        ],
                                      {
                                          "class": "content",
                                          "id": "parent_node_4_2"
                                        }
                                      )
        self.parentnode_4_3 = ParentNode("section",
                                         [
                                             self.leafnode5,
                                             self.leafnode6,
                                             self.leafnode7
                                            ],
                                         {
                                             "id": "parent_node_4_3",
                                             "class": "section"
                                            }
                                         )

        # Parent Nodes containg both leaf and parent children (lvl 3)
        self.parentnode_3_1 = ParentNode("div",
                                      [
                                          self.parentnode_4_1,
                                          self.leafnode8,
                                          self.parentnode_4_2,
                                        ],
                                      {
                                          "id": "parent_node_3_1",
                                          "class": "container"
                                        }
                                      )
        self.parentnode_3_2 = ParentNode("p",
                                         [
                                             self.leafnode9
                                            ]
                                         )
        self.parentnode_3_3 = ParentNode("article",
                                      [
                                          self.leafnode10,
                                          self.parentnode_4_3,
                                          self.leafnode11
                                        ],
                                      {
                                          "id": "parent_node_3_3",
                                          "class": "article"
                                        }
                                      )


    # Parent Nodes with Parent Children (lvl 2)
        self.parentnode_2_1 = ParentNode("main",
                                            [
                                                self.parentnode_3_1,
                                                self.parentnode_3_2
                                            ],
                                            {
                                                "id": "main_content"
                                            }
                                            )
        self.parentnode_2_2 = ParentNode("section",
                                         [
                                             self.parentnode_3_3,
                                            ],
                                         {
                                             "id": "secondary_content",
                                             "class": "secondary"
                                            }
                                         )
    # Top Parent Node (lvl 1)
        self.parentnode_1 = ParentNode("body",
                                       [
                                           self.parentnode_2_1,
                                           self.parentnode_2_2
                                        ],
                                       {
                                           "id": "body",
                                           "class": "page"
                                        }
                                       )


    def test_parent_to_html_no_tag(self):
        self.assertRaises(ValueError, self.parentnode_no_tag.to_html)
    
    def test_parent_to_html_no_children(self):
        self.assertRaises(ValueError, self.parentnode_no_children.to_html)

    def test_parent_to_html_recursion(self):
        self.assertEqual(self.parentnode_1.to_html(),
                          "<body id=body class=page>"
                            "<main id=main_content>"
                                "<div id=parent_node_3_1 class=container>"
                                    "<p id=parent_node_4_1>"
                                        "<a href=https://www.google.com id=link>"
                                        "This is a link."
                                        "</a>"
                                        "<p>"
                                        "Hello, world!"
                                        "</p>"
                                    "</p>"
                                    "<span class=highlight id=span_2>"
                                    "another span text."
                                    "</span>"
                                    "<div class=content id=parent_node_4_2>"
                                        "<h1 id=header_1>"
                                        "First Header"
                                        "</h1>"
                                        "<h2 id=header_2>"
                                        "cat_picture"
                                        "</h2>"
                                    "</div>"
                                "</div>"
                                "<p>"
                                    "<h1 class=header_1 id=header_1_2>"
                                    "more headers"
                                    "</h1>"
                                "</p>"
                            "</main>"
                            "<section id=secondary_content class=secondary>"
                                "<article id=parent_node_3_3 class=article>"
                                    "<p class=paragraph id=paragraph_last?>"
                                    "hopefully the last paragraph."
                                    "</p>"
                                    "<section id=parent_node_4_3 class=section>"
                                        "<span class=highlight>"
                                        "Some span text."
                                        "</span>"
                                        "<a href=https://example.com>"
                                        "Another link."
                                        "</a>"
                                        "<p class=description>"
                                        "Another Paragraph."
                                        "</p>"
                                    "</section>"
                                    "<h6>"
                                    "closing header"
                                    "</h6>"
                                "</article>"
                            "</section>"
                          "</body>"
                          )

