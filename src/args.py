import argparse

#Argument parser
parser = argparse.ArgumentParser()

fileParser = parser.add_argument_group("File Specifiers")
fileParser.add_argument("input", type=str, metavar='ifile', help="input file, needs to have .pynote extension")
fileParser.add_argument("-o", "--output", type=str, metavar='ofile', help="output file, needs to have .docx extension")
fileParser.add_argument("-j", "--json", type=str, metavar='JSON', default="~/Documents/GitHub/pyNote/configs/default.json", help="header JSON, default is ./configs/default.json")

# i need to fix the file paths so they work every where, MUST ADD THE OS.DIR() TO GET FILE PATH THIS IS NOT THE CORRECT SOLUTION IN LINE 8

debugParser = parser.add_argument_group("Debug Tools")
debugParser.add_argument("-s", "--settings", action='store_true', default=False, help="prints out the settings after processing the header")
debugParser.add_argument("-c", "--config", action='store_true', default=False, help="prints out the config json specified")
debugParser.add_argument("-v", '--void', action='store_true', default=False, help="doesn't create or edit the file")

_args = parser.parse_args()
