import re
from tagparsers.class_parsedvar import ParsedVar

def parse_var(tag: str) -> ParsedVar:

    """
        refer to readme even though it is deprecated

        vars can come in this format

        ~a\v=1\t+3 or !a\v=1\t+3

        \v={compound text string}
        \v=word
        \v=\l
        \v=\h+3
        [~,!,][subtype]\v=[{},text,style,size]
    """

    # this will follow the hierarchy

    #check for compound text string that includes the thing urg ill have to return another parser
    
    # i need to determine the ptype
    # i need to determine the subtype
    # i need to determine the assignemed

    # i need to separate at the equals
    notassigned, assigned = tag.split("=")
    