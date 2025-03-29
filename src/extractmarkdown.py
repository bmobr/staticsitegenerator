from htmlnode import *
from textnode import *
# for regular expressions
import re

# takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images. 
def extract_markdown_images(text):
    new_text = []
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        new_text.append((match[0], match[1]))
    return new_text


# extracts markdown links instead of images. It should return tuples of anchor text and URLs.
def extract_markdown_links(text):
    new_text = []
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        new_text.append((match[0], match[1]))
    return new_text
    

