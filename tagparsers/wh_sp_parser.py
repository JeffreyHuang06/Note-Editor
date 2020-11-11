import re
from tagparsers.class_parsetag import ParsedTag

# _rules is the settingsjson

def parse_wh_sp(tag : str) -> ParsedTag:
    
    if len(re.findall("\\\\bull", tag)): #bullet

        if tag == "\\bull":
            return ParsedTag("tag", 1, "is_bull = True", "__new_bullet__")
        elif tag == "\\\\bull":
            return ParsedTag("tag", 1, "is_bull = False", "__remove_bullet__")
    
    elif len(re.findall("\\\\plain", tag)): #plain
        return ParsedTag("invtag", 1, "is_plain = True")

        #oh god coding in all the special behaviours is gonna fucking succcccccccc
    
    elif len(re.findall("\\\\div", tag)): #div
        ...
    
    elif len(re.findall("\\\\ind", tag)): #ind
        ...