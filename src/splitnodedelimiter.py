from htmlnode import *
from textnode import *

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