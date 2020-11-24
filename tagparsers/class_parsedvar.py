class ParsedVar:

    # [~,!,][subtype]\v=[{},text,style,size]

    """
    args format:

    pytype - 
    is whether the assiged is a {} - complex, text, style, or size

    sp_type - 
    is whether it is temp, inv, or none

    subtype -
    the varaible name if any
    eg. t/v

    assigned -
    the assigned thing
    
    """

    def __init__(self, ptype: str, sp_type: str, subtype: str, assigned: str):
        
        if ptype == "complex":
            exit("this hasnt been implemented yet")
        
        elif ptype == "text":
            ...
        
        elif ptype == "style":
            ...
        
        elif ptype == "size":
            ...