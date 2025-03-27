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
        