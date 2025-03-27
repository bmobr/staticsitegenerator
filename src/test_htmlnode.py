import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "some text", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("<a>", "some text", None, {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = HTMLNode("a", "some text", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "some other text", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("a", "some text", None, {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "HTMLNode: (tag=a, value=some text, children=None, props={'href': 'https://www.google.com'})")

    def test_props_to_html(self):
        node = HTMLNode("a", "some text", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html(self):
        parent_node = ParentNode("div", [LeafNode("span", "child")], props={"class": "example", "id": "main"})
        self.assertEqual(parent_node.props_to_html(), ' class="example" id="main"')

    def test_props_to_html_empty_props(self):
        parent_node = ParentNode("div", [LeafNode("span", "child")], props={})
        self.assertEqual

    def test_leaf_to_html(self):
        node  = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    def test_leaf_eq(self):
        node  = LeafNode("p", "Hello world")
        node2 = LeafNode("p", "Hello world")
        self.assertEqual(node, node2)
    
    def test_leaft_ne(self):
        node  = LeafNode("p", "Hello world")
        node2 = LeafNode("p", "Hello world2")
        self.assertNotEqual(node, node2)
    
    def test_leaf_repr(self):
        node  = LeafNode("p", "Hello world")
        self.assertEqual(node.__repr__(), "LeafNode: (tag=p, value=Hello world, props=None)")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_empty_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertTrue("children" in str(context.exception))

    def test_nested_parent_nodes(self):
        grandchild_node = LeafNode("p", "Text")
        child_node = ParentNode("span", [grandchild_node])
        main_node = ParentNode("div", [child_node])
        self.assertEqual(
            main_node.to_html(),
            "<div><span><p>Text</p></span></div>"
        )

if __name__ == "__main__":
    unittest.main()