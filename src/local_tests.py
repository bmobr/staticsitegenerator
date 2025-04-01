from textnode import *
from splitnodes import *
from converttonodes import *
from splitnodedelimiter import *
from extractmarkdown import *
from blocktype import *

def split_image_test1():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    for node in new_nodes:
        print(f"{node}\n")

def split_image_test2():
    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_image([node])
    for node in new_nodes:
        print(f"{node}\n")
    

def split_link_test1():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    for node in new_nodes:
        print(f"{node}\n")

def converttonodes_test1():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text)
    new_nodes = text_to_textnodes(text)
    for node in new_nodes:
        print(f"{node}\n")

def split_delimiter_test1():
    text = "This is **text** with an _italic_ word and a `code block`"   
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    for node in new_nodes:
        print(f"{node}\n")

def markdown_to_blocks_test1():
    text = """
    # This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    """
    # print(text)
    new_nodes = markdown_to_blocks(text)
    i = 0
    for node in new_nodes:
        i += 1
        print(f"{i}. {node}")

def markdown_to_blocks_test2():
    md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
    new_nodes = markdown_to_blocks(md)
    i = 0
    for node in new_nodes:
        i += 1
        print(f"{i}. {node}")

def test_block_to_block_type():
    print(block_to_block_type("hello") == BlockType.PARAGRAPH)
    print(block_to_block_type("# hello") == BlockType.HEADING)
    print(block_to_block_type("### hello") == BlockType.HEADING)
    print(block_to_block_type("###hello") == BlockType.HEADING)
    print(block_to_block_type("- hello\n- hello") == BlockType.UNORDERED_LIST)
    print(block_to_block_type("1. hello\n2. hello") == BlockType.ORDERED_LIST)
    print(block_to_block_type("```\nhello\n```") == BlockType.CODE)
    print(block_to_block_type(">hello\n> hello again") == BlockType.QUOTE)
    

def main():
    #split_image_test1()   
    #split_image_test2()    
    #split_link_test1()   
    #converttonodes_test1()
    #split_delimiter_test1()
    #markdown_to_blocks_test1()
    #markdown_to_blocks_test2()
    test_block_to_block_type()

if __name__ == "__main__":
    main()