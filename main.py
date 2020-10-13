import sys, os, json, argparse

from docx import Document
from docx.shared import Inches

from interpreters import interHeader as iH
from interpreters import interBody as iB

from utils import debugtools as dbg

doc = Document()

#Argument parser
parser = argparse.ArgumentParser()

fileParser = parser.add_argument_group("File Specifiers")
fileParser.add_argument("input", type=str, metavar='ifile', help="input file, needs to have .pynote extension")
fileParser.add_argument("-o", "--output", type=str, metavar='ofile', help="output file, needs to have .docx extension")
fileParser.add_argument("-j", "--json", type=str, metavar='JSON', default="./configs/default.json", help="header JSON, default is ./configs/default.json")

debugParser = parser.add_argument_group("Debug Tools")
debugParser.add_argument("-s", "--settings", action='store_true', default=False, help="prints out the settings after processing the header")
debugParser.add_argument("-c", "--config", action='store_true', default=False, help="prints out the config json specified")
debugParser.add_argument("-v", '--void', action='store_true', default=False, help="doesn't create or edit the file")

# fargs = fileParser.parse_args()
# dargs = debugParser.parse_args()
args = parser.parse_args()

#Get the selected pynote file
if ".pynote" not in (ifile := args.input):
    exit("Error: Input file must have .pynote extension")

with open(args.input,"r") as fin:
    tokens = fin.readlines()

#JSON Settings
with open(args.json, "r") as jsn:
    settings = json.load(jsn)

#DEBUGTOOLS
dbg.init(args)


#Read Header
iH.init(settings)

dbg.c_settings(settings) #DEBUGTOOLS

for ind, line in enumerate(tokens):
    if iH.headerMode == False and iH.foundHeader == True: break
    iH.checkForHeader(ind, line[:-1]) #removes the endl

settings = iH.settings

dbg.c_settings(settings) #DEBUGTOOLS



# Strip the header declarations from the lines
tokens = tokens[ind:]



#Check to make sure there's more than a header
if tokens[0] == '\end':
    exit("Error: No body present")



#Interpret the body
iB.init(settings, doc)

for ind, line in enumerate(tokens):
    iB.parseLine(ind, line)



#SAVING AND WRITING THE DOCUMENT
dbg.c_void() #DEBUGTOOLS

if (ofile := args.output) == None:
    doc.save(f'./{ofile[:-6]}docx')

else:
    if ".docx" in ofile:
        doc.save(f'{ofile}')
    else:
        exit("Error: Output file must have .docx extension")