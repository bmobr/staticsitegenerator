from textnode import *
from htmlnode import *  
from extractmarkdown import *

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
