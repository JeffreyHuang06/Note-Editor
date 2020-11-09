import re

def parse_wh_sp(tag : str) -> str:
    
    if len(re.findall("\\\\bull", tag)): #bullet
        ...
    
    elif len(re.findall("\\\\plain", tag)): #plain
        ...
    
    elif len(re.findall("\\\\div", tag)): #div
        ...
    
    elif len(re.findall("\\\\ind", tag)): #ind
        ...