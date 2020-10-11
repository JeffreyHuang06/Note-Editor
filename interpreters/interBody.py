settings = 0

is_h = False
is_t = False
is_r = False
is_l = False
is_b = False
is_i = False
is_emph = False

def init(settingjson : dict):
    global settings
    global is_h, is_t, is_r, is_l, is_b, is_r, is_i, is_emph
    settings = settingjson

    #create the bool settgins possibly
    


def parseLine(ind : int, line : str):
    tokens = line.split()
    tokens.append('\n')
    
    for tag in tokens:
        if tag == r'\h':
            pass
        