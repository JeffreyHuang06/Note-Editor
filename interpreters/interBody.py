from docx.shared import Pt
import typing
import re

from tagparsers import wh_sp_parser
from tagparsers import var_parser
from tagparsers.class_parsedtag import ParsedTag

from src.isdict import _is

_settings = dict()
document = 0

def init(doc):
    global _settings, document

    from src.settings import _settings as settings
    _settings = settings
    document = doc

    # create the bool settgins possibly


def split_line(line: str) -> typing.List[str]:
    tokens = line.split()
    lenline = len(line)

    # find all tags
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

    # make another list of the spearated inds
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
        (lastind, lenline - 1)
    )

    # get the actual strings from the inds
    splines = []
    for inds in sepinds:
        splines.append(
            line[inds[0]: inds[1]]
        )

    return splines


def parse_tag(tag: str):

    """
        this will return text, or it will return a rule change, in the form of a tuple

        tuple format:
            (
                length of rules
                rule changes in teh form of executes
                text to place in, if none then return None
            )
    """

    """
        check for whitespace and special first

        hierarchy goes:
            variable
            style
            size
            special 
    """

    if "\\" in tag and not _is["is_plain"]:  # could be a tag

        re_wh_sp = re.findall("bull|plain|div|ind", tag)
        re_var = re.findall("\\\\v=", tag)  # returns type: list
        re_style = re.findall("\\\\[bli]|^\\\\\\[", tag) #this regex is despicable
        re_size = re.findall("\\\\[htr]", tag)

        if len(re_wh_sp):  # it will only accept inds now
            return wh_sp_parser.parse_wh_sp(tag)

        elif len(re_var):
            return var_parser.parse_var(tag)
            
    else:
        ...


def parseLine(lineind: int, line: str):
    # get the splitted line
    splines = split_line(line)  # each "token" for the parser to parse
    docxline = document.add_paragraph("")  # make a new line to add

    for ind, token in enumerate(splines):
        res = parse_tag(token)

        # __ __ dunders are special
        

