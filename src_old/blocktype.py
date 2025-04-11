from enum import Enum

# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
# Create a BlockType enum with the block types from above.

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

# takes a single block of markdown text as input and returns the BlockType representing the type of block it is. 
# You can assume all leading and trailing whitespace was already stripped 
def block_to_block_type(markdown_block):           
    if markdown_block.startswith("#"):
        i = 0
        # count the number of # characters
        for char in markdown_block:
            if char == "#":
                i += 1
            else:
                break
        # if the number of # characters is less than or equal to 6, and it's followed by a space, it's a heading
        if i<=6 and i>0 and len(markdown_block)>i and markdown_block[i] == " ":
            return BlockType.HEADING
        else:   
            return BlockType.PARAGRAPH
    elif markdown_block.startswith("-"):
        # check if all lines start with -
        lines = markdown_block.split("\n")
        is_valid = True
        for line in lines:
            if not line.startswith("- "):
                is_valid = False
                break            
        if is_valid:    
            return BlockType.UNORDERED_LIST
        else:   
            return BlockType.PARAGRAPH        
    elif markdown_block.startswith("1."):
        # check if all lines start with number and a dot
        i = 1
        is_valid = True
        lines = markdown_block.split("\n")
        for line in lines:
            if not line.startswith(f"{i}. "):
                is_valid = False
                break
            else:
                i += 1
        if is_valid:    
            return BlockType.ORDERED_LIST
        else:   
            return BlockType.PARAGRAPH     
    elif markdown_block.startswith("```"):
        # check if the last line is ```
        lines = markdown_block.split("\n")        
        if lines[-1] == "```":            
            return BlockType.CODE
        else:
            return BlockType.PARAGRAPH
    elif markdown_block.startswith(">"):
        # check if all lines start with >
        lines = markdown_block.split("\n")
        is_valid = True
        for line in lines:
            if not line.startswith(">"):
                is_valid = False
                break            
        if is_valid:    
            return BlockType.QUOTE
        else:   
            return BlockType.PARAGRAPH       
    # if none of the above, it's a paragraph   
    else:
        return BlockType.PARAGRAPH
    
