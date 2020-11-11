import re
from tagparsers.class_parsetag import ParsedTag

def parse_wh_sp(tag : str) -> ParsedTag:
    
    if len(re.findall("\\\\bull", tag)): #bullet

        if tag == "\\bull":
            return ParsedTag("tag", 1, {"is_bull": True}, "__new_bullet__")

        elif tag == "\\\\bull":
            return ParsedTag("tag", 1, {"is_bull": False}, "__remove_bullet__")

    elif len(re.findall("\\\\plain", tag)): #plain

        if tag == "\\plain":
            return ParsedTag("invtag", 1, {"is_plain": True})
        elif tag == "\\\\plain":
            return ParsedTag("invtag", 1, {"is_plain": False})

        #oh god coding in all the special behaviours is gonna fucking succcccccccc
    
    elif len(re.findall("\\\\div", tag)): #div

        #urgg fuck im gonna have to make a style cache fucking shit goddammit

        # NOT YET IPLEMENTED
        return ParsedTag("invtag", 0)
    
    elif len(re.findall("\\\\ind", tag)): #ind

        if tag == "\\ind":
            return ParsedTag("invtag", 1, {"is_ind": True})

        elif tag == "\\\\ind":
            return ParsedTag("invtag", 1, {"is_ind": False})