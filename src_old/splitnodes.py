from textnode import *
from htmlnode import *  
# for regular expressions
import re


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)    
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

# It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, 
# where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. 
# For example, given the following input:
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# becomes
# [
#    TextNode("This is text with a ", TextType.TEXT),
#    TextNode("code block", TextType.CODE),
#    TextNode(" word", TextType.TEXT),
#]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Now handle TEXT nodes
        parts = []
        remaining_text = old_node.text
        
        # While there's still text to process
        while delimiter in remaining_text:
            # Find the opening delimiter
            start_index = remaining_text.find(delimiter)
            if start_index == -1:
                break
                
            # Add text before the delimiter as TEXT type
            if start_index > 0:
                parts.append((remaining_text[:start_index], TextType.TEXT))
                
            # Find the closing delimiter
            end_index = remaining_text.find(delimiter, start_index + len(delimiter))
            if end_index == -1:
                raise Exception(f"Missing closing delimiter: {delimiter}")
                
            # Add text between delimiters with the specified type
            content = remaining_text[start_index + len(delimiter):end_index]
            parts.append((content, text_type))
            
            # Update remaining text
            remaining_text = remaining_text[end_index + len(delimiter):]
            
        # Add any remaining text as TEXT type
        if remaining_text:
            parts.append((remaining_text, TextType.TEXT))
            
        # Add the new nodes to the list
        for part in parts:
            new_nodes.append(TextNode(part[0], part[1]))
            
    return new_nodes

# takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images. 
def extract_markdown_images(text):
    # new_text = []
    # the re.findall() function returns a list of tuples
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # for match in matches:
    #    new_text.append((match[0], match[1]))
    return matches


# extracts markdown links instead of images. It should return tuples of anchor text and URLs.
def extract_markdown_links(text):
    # new_text = []
    # the re.findall() function returns a list of tuples
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # for match in matches:
    #    new_text.append((match[0], match[1]))
    return matches
    

# takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings. 
def markdown_to_blocks(markdown):
    # split by double newlines
    text_nodes = markdown.split("\n\n")
    clean_nodes = []
    for node in text_nodes: 
        # remove leading and trailing whitespace
        node = node.strip()    
        # remove leading and trailing spaces from each line
        if node.find("\n") != -1:
            lines = node.split("\n")
            # remove leading and trailing whitespace from each line
            stripped_lines = [line.strip() for line in lines]
            # join the lines back into a single string
            node = "\n".join(stripped_lines)
        # add the node to the list
        if node:             
            clean_nodes.append(node)
    
    return clean_nodes

# split raw markdown text into TextNodes based on images and links.
# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:             
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
                
        text = old_node.text
        temp_text = text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            image_node = TextNode(image[0], TextType.IMAGE, image[1])
            temp_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if temp_text[0] != "":                
                new_nodes.append(TextNode(temp_text[0], TextType.TEXT))
            new_nodes.append(image_node)
            if len(temp_text) > 1:
                text = temp_text[1]
        if len(text) > 0 and text != "":   
            new_nodes.append(TextNode(text, TextType.TEXT))            
        
    return new_nodes
            
    
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:             
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
                
        text = old_node.text
        temp_text = text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            link_node = TextNode(link[0], TextType.LINK, link[1])
            temp_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if temp_text[0] != "":                
                new_nodes.append(TextNode(temp_text[0], TextType.TEXT))
            new_nodes.append(link_node)
            if len(temp_text) > 1:
                text = temp_text[1]
        if len(text) > 0 and text != "":   
            new_nodes.append(TextNode(text, TextType.TEXT))            
        
    return new_nodes

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


