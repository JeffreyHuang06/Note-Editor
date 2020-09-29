settings = 0
def init(settingjson : dict):
    global settings
    settings = settingjson

#INTERPRETTING THE HEADING
headerMode = False
foundHeader = False

def checkForHeader(ind : int, word : str):
    global headerMode, foundHeader

    #Check for \header
    if ind == 0 and word == r'\header':
        headerMode = True
        foundHeader = True
        return

    #Check for \end
    if word == r'\end' and headerMode == True:
        headerMode = False
        return

    #In Headermode currently
    elif headerMode == True:
        #Check if it had keyword
        if '\\' in word:
            pass
        
        #Normal declaration
        else:
            word_tokens = word.split('=', 1)
            tag = word_tokens[0]

            if tag == 'v':
                settings[tag][""] = word_tokens[1]
            else:
                settings[tag][""] = int(word_tokens[1])
