from textnode import *
from splitnodedelimiter import *
from splitnodes import *

# convert a raw string of markdown-flavored text into a list of TextNode objects
# This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
# [
#    TextNode("This is ", TextType.TEXT),
#    TextNode("text", TextType.BOLD),
#    TextNode(" with an ", TextType.TEXT),
#    TextNode("italic", TextType.ITALIC),
#    TextNode(" word and a ", TextType.TEXT),
#    TextNode("code block", TextType.CODE),
#    TextNode(" and an ", TextType.TEXT),
#    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#    TextNode(" and a ", TextType.TEXT),
#    TextNode("link", TextType.LINK, "https://boot.dev"),
# ]

def text_to_textnodes(text):
    new_nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "\n", TextType.TEXT)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)    
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

