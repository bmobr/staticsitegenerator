from htmlnode import *
from textnode import *
from splitnodes import *
from blocktype import *
from texttohtmlnode import *

# converts a full markdown document into a single parent HTMLNode
# That one parent HTMLNode should contain many child HTMLNode objects representing the nested elements.
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_html_blocks = []  # List to hold all block nodes
    for block in blocks:
        print(block)
        block_type = block_to_block_type(block)
        print(block_type)
        if block_type == BlockType.PARAGRAPH:
            html_block = text_to_paragraph_nodes(block)
        elif block_type == BlockType.HEADING:
            html_block = text_to_heading_nodes(block)
        elif block_type == BlockType.CODE:
            html_block = text_to_code_nodes(block)
        elif block_type == BlockType.QUOTE:
            html_block = text_to_quote_nodes(block)
        elif block_type == BlockType.UNORDERED_LIST:
            html_block = text_to_ul_nodes(block)
        elif block_type == BlockType.ORDERED_LIST:
            html_block = text_to_ol_nodes(block)        

        all_html_blocks.append(html_block)
        print(html_block)
    # Create parent div and return
    parent_node = HTMLNode("div", None, all_html_blocks, {})
    return parent_node
    

def text_to_children(text):
    pass

def text_to_paragraph_nodes(text):
    new_text = "<p>"
    text = text.strip()
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        print(f"node: {node}")
        new_text += node.to_html()
    new_text += "</p>"
    return new_text

def text_to_heading_nodes(text):
    pass

def text_to_code_nodes(text):
    pass    

def text_to_quote_nodes(text):
    pass

def text_to_ul_nodes(text):
    pass

def text_to_ol_nodes(text):
    pass

def test():
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    node = markdown_to_html_node(md)
    #html = node.to_html()
    #print(html)


if __name__ == "__main__":
    test()