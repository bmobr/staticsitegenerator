from htmlnode import *
from textnode import *
from converttonodes import *
# for regular expressions
import re

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