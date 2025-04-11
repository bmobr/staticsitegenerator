import unittest
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("hello"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("# hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("- hello\n- hello"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. hello\n2. hello"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("```\nhello\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> hello\n> hello again"), BlockType.QUOTE)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Multiple lines\nin a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#This is not a heading because no space"), BlockType.PARAGRAPH)
        
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading level 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading level 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading level 6"), BlockType.HEADING)
        # Too many # characters should be a paragraph
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.PARAGRAPH)
        
    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\nMultiple lines\nof code\n```"), BlockType.CODE)
        # Not a code block if it doesn't end with backticks
        self.assertEqual(block_to_block_type("```\ncode without closing backticks"), BlockType.PARAGRAPH)

    def test_quote(self):
        self.assertEqual(block_to_block_type(">This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">Line 1\n>Line 2"), BlockType.QUOTE)
        # Not a quote if not all lines start with >
        self.assertEqual(block_to_block_type(">Line 1\nLine 2"), BlockType.PARAGRAPH)    

if __name__ == "__main__":
    unittest.main()