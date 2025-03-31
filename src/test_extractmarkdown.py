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

    def test_extract_markdown_images(self):
        # Test 1: Simple case with two images
        text = "This is text with a ![cat](https://example.com/cat.png) and ![dog](https://example.com/dog.png)"
        expected = [('cat', 'https://example.com/cat.png'), ('dog', 'https://example.com/dog.png')]
        self.assertListEqual(extract_markdown_images(text), expected)
        
        # Test 2: No images in the text
        text = "This is text without any images or special markdown."
        expected = []
        self.assertListEqual(extract_markdown_images(text), expected)

        # Test 3: Edge case with empty alt text
        text = "![](https://example.com/emptyalt.png)"
        expected = [('', 'https://example.com/emptyalt.png')]
        self.assertListEqual(extract_markdown_images(text), expected)
        
        # Test 4: Complex URL with query parameters
        text = "![chart](https://example.com/chart.png?width=500&height=400)"
        expected = [('chart', 'https://example.com/chart.png?width=500&height=400')]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        # Test 5: Simple links
        text = "This is a [link to google](https://www.google.com) and a [link to boot dev](https://www.boot.dev)"
        expected = [('link to google', 'https://www.google.com'), ('link to boot dev', 'https://www.boot.dev')]
        self.assertListEqual(extract_markdown_links(text), expected)
        
        # Test 6: Text with no links
        text = "Just normal text, no links here!"
        expected = []
        self.assertListEqual(extract_markdown_links(text), expected)
        
        # Test 7: Links with special characters
        text = "[search link](https://example.com/search?q=markdown&lang=en)"
        expected = [('search link', 'https://example.com/search?q=markdown&lang=en')]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "Just one block with no empty lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one block with no empty lines"])

    def test_multiple_newlines_between_blocks(self):
        md = "First block\n\n\n\nSecond block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_code_blocks(self):
        md = "```python\nprint('Hello, world!')\n```"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["```python\nprint('Hello, world!')\n```"])
    
    
if __name__ == "__main__":
    unittest.main()