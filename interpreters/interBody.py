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
    


def parseLine(lineind : int, line : str):
    #feed the thing char by char in order to make whitespace
    #make a first run to get all the tags, then find them, then add the sentences
    tokens = line.split()
    tokeninds = []
    lenline = len(line)
    #i could use regex... but i wont

    #find all tags
    tags = [i for i in tokens if '\\' in i]
    taginds = []
    startind = 0
    for tag in tags:
        ind = line.find(tag, startind, lenline) # get the inds and lengths of all the tags
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
            line[inds[0] : inds[1]]
        )
    
