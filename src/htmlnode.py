class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):        
        if not self.props:
            return ""
        else:
            props_values = ""
            for key, value in self.props.items():
                props_values += f' {key}="{str(value)}"'
            return props_values
    
    def __repr__(self):
        return(f"HTMLNode: (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})") 
    
    def __eq__(self, value):
        if self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props:
            return True
        else:
            return False

# Create a child class of HTMLNode called LeafNode. Its constructor should differ slightly from the HTMLNode class because:
# It should not allow for any children
# The value data member should be required (and tag even though the tag's value may be None)
# Use the super() function to call the constructor of the HTMLNode class.
# Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).
# If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
# If there is no tag (e.g. it's None), the value should be returned as raw text.
# Otherwise, it should render an HTML tag.
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return  f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return (f"LeafNode: (tag={self.tag}, value={self.value}, props={self.props})") 


# Create another child class of HTMLNode called ParentNode. Its constructor should differ from HTMLNode in that:
# The tag and children arguments are not optional
# It doesn't take a value argument
# props is optional
# (It's the exact opposite of the LeafNode class)
# Add a .to_html method.
# If the object doesn't have a tag, raise a ValueError.
# If children is a missing value, raise a ValueError with a different message.
# Otherwise, return a string representing the HTML tag of the node and its children. 
# This should be a recursive method (each recursion being called on a nested child node). 
# I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)  
        if self.tag is None or self.tag == "":
            raise ValueError("Parent node must have a tag")
        elif self.children is None or self.children == []:
            raise ValueError("Parent node must have children")

    def to_html(self):
        children = "".join([child.to_html() for child in self.children])            
        # child_list =[]
        # for child in self.children:
            # child_list.append(child.to_html())
        # children = "".join(child_list)
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

    def __repr__(self):
        return (f"ParentNode: (tag={self.tag}, children={self.children}, props={self.props})")
        