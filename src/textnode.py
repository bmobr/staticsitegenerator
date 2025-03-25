from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "__Italic text__"
    CODE = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![image alt text](image url)"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"        