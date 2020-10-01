import sys

settings = 0
def init(settingjson : dict):
    global settings
    settings = settingjson

#INTERPRETTING THE HEADING
headerMode = False
foundHeader = False

digits = [i for i in range(10)]

def checkForHeader(ind : int, token : str):
    global headerMode, foundHeader
    global digits

    #Check for \header
    if ind == 0 and token == '\header':
        headerMode = True
        foundHeader = True
        return

    #Check for \end
    if token == '\end' and headerMode == True:
        headerMode = False
        return

    #In Headermode currently
    elif headerMode == True:

        word_tokens = token.split('=', 1)
        tag = word_tokens[0]

        #Check if it had keyword
        if '\\' in token:
            #error checking

            if '\\' in tag: exit(f"Line {ind+1}: Intial backslashes not allowed in Header Declaration")
            
            #checking if there is a subtype
            for char in tag:
                if char in digits: exit(f"Line {ind+1}: Subtyping not allowed in Header Declaration")
            
        
        #Normal declaration
        else:

            #variable declaration
            if tag == 'v':
                settings[tag][""] = word_tokens[1]

            #global rules
            elif '-' in tag:
                settings[tag] = word_tokens[1]
            
            #size rules
            else:
                settings[tag][""] = int(word_tokens[1])
