from textnode import *
from splitnodes import *
from converttonodes import *
from splitnodedelimiter import *

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

def main():
    #split_image_test1()   
    #split_image_test2()    
    #split_link_test1()   
    converttonodes_test1()
    #split_delimiter_test1()

if __name__ == "__main__":
    main()