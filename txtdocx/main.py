#transfers it from txt, therefore no tags
import typing, argparse
from docx import Document 
from docx.shared import Inches

from utils import debugtools as dbg

parser = argparse.ArgumentParser()

fileParser = parser.add_argument_group("File Specifiers")
fileParser.add_argument("input", type=str, metavar='ifile', help="input file, needs to have .pynote extension")
fileParser.add_argument("-o", "--output", type=str, metavar='ofile', help="output file, needs to have .docx extension")
fileParser.add_argument("-j", "--json", type=str, metavar='JSON', default="./configs/default.json", help="header JSON, default is ./configs/default.json")

debugParser = parser.add_argument_group("Debug Tools")
debugParser.add_argument("-s", "--settings", action='store_true', default=False, help="prints out the settings after processing the header")
debugParser.add_argument("-c", "--config", action='store_true', default=False, help="prints out the config json specified")
debugParser.add_argument("-v", '--void', action='store_true', default=False, help="doesn't create or edit the file")

args = parser.parse_args()

#make the document
doc = Document()

#open the document
text=''
with open(args.input, "r+") as fin:
    text = fin.read()

#DEBUG TOOLS
dbg.init(args)

#add the text
par = doc.add_paragraph(text)

dbg.c_void() #DEBUGTOOLS

if (ofile := args.output) == None:
    doc.save(f'{args.input[:-4]}.docx')

else:
    if ".docx" in ofile:
        doc.save(f'{ofile}')
    else:
        exit("Error: Output file must have .docx extension")

exit()