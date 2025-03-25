class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_values = ""
        if self.props is None:
            return props_values
        else:
            for key, value in self.props.items():
                props_values += f" {key}='{value}'"
        return props_values
    
    def __repr__(self):
        return(f"HTMLNode: (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})") 
    
    def __eq__(self, value):
        if self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props:
            return True
        else:
            return False
