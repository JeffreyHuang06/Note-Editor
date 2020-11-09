from docx.shared import Pt
import typing
import re
from tagparsers import *

settings = dict()
document = 0

_is = {
    "is_h" : False,
    "is_t" : False,
    "is_r" : False,
    "is_l" : False,
    "is_b" : False,
    "is_i" : False,
    "is_emph" : False,
    "is_plain" : False
}

def init(settingjson : dict, doc):
    global settings, document
    # global is_h, is_t, is_r, is_l, is_b, is_r, is_i, is_emph, is_plain
    global _is
    settings = settingjson
    document = doc

    #create the bool settgins possibly
    
def split_line(line: str) -> typing.List[str]:
    tokens = line.split()
    lenline = len(line)

    #find all tags
    tags = [i for i in tokens if '\\' in i]
    taginds = []
    startind = 0
    for tag in tags:
        # get the inds and lengths of all the tags
        ind = line.find(tag, startind, lenline)
        taginds.append(
            (ind, ind + len(tag))
        )
        startind += ind + len(tag)

    #make another list of the spearated inds
    sepinds = []
    lastind = 0
    for inds in taginds:
        sepinds.append(
            (lastind, inds[0])
        )
        sepinds.append(
            (inds[0], inds[1])
        )
        lastind = inds[1]
    sepinds.append(
        (lastind, lenline-1)
    )

    #get the actual strings from the inds
    splines = []
    for inds in sepinds:
        splines.append(
            line[inds[0]: inds[1]]
        )
    
    return splines



def parse_tag(tag: str) -> str: #this will return either void or a new text

    #check if style or assignment or both
    # re_var = len(re.findall("\\\\v=", tag))
    # re_style = len(re.findall("\\\\[bli]|^I\\[", tag))
    # re_size = len(re.findall("[htr]", tag))
    # re_special = len(re.findall("bull|plain|div"))
    # re_whitesp = len(re.findall("tab|ind"))

    """
        check for whitespace and special first

        hierarchy goes:
            variable
            style
            size
            special 
    """

    if "\\" in tag and not _is["is_plain"]: #could be a tag
            re_wh_sp = re.findall("bull|plain|div|ind", tag)
            re_var = re.findall("\\\\v=", tag) # returns type: list
            re_style = re.findall("\\\\[bli]|^\\[", tag)
            re_size = re.findall("\\\\[htr]", tag)

            if len(re_wh_sp): #it will only accept inds now
                return wh_sp_parser.parse_wh_sp(tag)

    else:
        pass

def parseLine(lineind : int, line : str):
    # get the splitted line
    splines = split_line(line) # each "token" for the parser to parse
    docxline = document.add_paragraph("") #make a new line to add
    
    #loop through everything
    for ind, token in enumerate(splines):
        
        docxphrase = docxline.add_run()

        parse_tag(token)