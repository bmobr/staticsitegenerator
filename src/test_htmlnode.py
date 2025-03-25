import unittest

from htmlnode import HTMLNode

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
        self.assertEqual(node.props_to_html(), " href='https://www.google.com'")

if __name__ == "__main__":
    unittest.main()