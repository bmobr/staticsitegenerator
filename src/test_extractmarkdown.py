import unittest
from extractmarkdown import *
from htmlnode import *
from textnode import *

class TestExtractMarkdown(unittest.TestCase):
  
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_images(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://example.com)")
        self.assertListEqual([("link", "https://example.com")], matches) 

    def test_extract_markdown_links_no_links(self):
        matches = extract_markdown_links("This is text with no links")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_various_images(self):
        matches = extract_markdown_images(
            "This is text with an ![some image](https://i.imgur.com/zjjcJKZ.png) and another ![another image](https://example.com)"
        )
        self.assertListEqual([("some image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", "https://example.com")], matches)

if __name__ == "__main__":
    unittest.main()