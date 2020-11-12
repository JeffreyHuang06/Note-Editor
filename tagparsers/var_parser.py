import re
from tagparsers.class_parsetag import ParsedTag

def parse_var(tag: str) -> ParsedTag:

    """
        refer to readme even though it is deprecated

        vars can come in this format

        ~3\v=1\t+3 or !3\v=1\t+3

        \v={compound text string}
        \v=word
        \v=\l
        \v=\h+3
        [~,!,][subtype]\v=[{},text,style,size]
    """

    ...