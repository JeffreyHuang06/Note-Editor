from docx.shared import Pt

settings = 0
document = 0

is_h = False
is_t = False
is_r = False
is_l = False
is_b = False
is_i = False
is_emph = False

def init(settingjson : dict, doc):
    global settings, document
    global is_h, is_t, is_r, is_l, is_b, is_r, is_i, is_emph
    settings = settingjson
    document = doc

    #create the bool settgins possibly
    


def parseLine(ind : int, line : str):
    #feed the thing char by char in order to make whitespace
    #make a first run to get all the tags, then find them, then add the sentences
    tokens = line.split()
    tokeninds = []
    #i could use regex... but i wont

    #find all tags
    tagMode = False
    lastind = 0
    for ind, char in enumerate(line):
        if tagMode:
            if char == ' ':
                lastind = ind + 1
                tagMode = False
        else:
            if char == '\\':
                tagMode = True
                tokeninds.append((lastind, ind))
    tokeninds.append((lastind, len(line)))

    #separate into lists of tags and lines
    splittedLine = []
    lastind = 0
