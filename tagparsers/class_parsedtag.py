class ParsedTag:

    """
    args format

    invtag -
        length of tag rules
        tag rules

    tag -
        length of tag rules
        tag rules
        text

    text -
        text

    """

    def __init__(self, ptype: str, *args):
        if ptype == "invtag":
            numrules = args[0]
            self.rules = args[1:numrules+1]

        elif ptype == "tag":
            numrules = args[0]
            self.rules = args[1:numrules+1]
            self.text = args[-1]

        elif ptype == "text":
            self.text = args[0]

        else:
            raise Exception("invalid ptype")

    # i will need some function to return a string that will be executed by teh interbody stream