import sys
import re

_settings = dict()

def init():
    global _settings

    from src.settings import _settings as settings
    _settings = settings

#INTERPRETTING THE HEADING
headerMode = False
foundHeader = False

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

            #checking if there is a subtype
            if len(re.findall("[0-9]", tag)):
                exit(f"Line {ind+1}: Subtyping not allowed in Header Declaration")

            subtags = tag.split('\\')
            maintag = subtags.pop(0)
            keyword = subtags[0] # might change later if keywords get more complex

            _settings["keywords"][keyword].update({word_tokens[1] : maintag}) # will need to be changed in order to expand this, like adding another level for multiple formats and also linking it to vars
        
        #Normal declaration
        else:

            #variable declaration
            if tag == 'v':
                _settings[tag][""] = word_tokens[1]

            #global rules
            elif '-' in tag:
                _settings[tag] = word_tokens[1]
            
            #size rules
            else:
                _settings[tag][""] = int(word_tokens[1])
