import sys, os, json, argparse

from docx import Document
from docx.shared import Inches

from interpreters import interHeader as iH
from interpreters import interBody as iB

from src.args import _args
from src.settings import _settings

from utils import debugtools as dbg

doc = Document()

#Get the selected pynote file
if ".txt" in (ifile := _args.input):
    import txtdocx.main #transfer the control flow

elif ".pynote" in ifile:
    pass
else:
    exit("Error: Input file must have .pynote or .txt extension")

with open(_args.input, "r") as fin:
    tokens = fin.readlines()

#Read Header
iH.init()

dbg.c_config() #DEBUGTOOLS

for ind, line in enumerate(tokens):
    if iH.headerMode == False and iH.foundHeader == True: break
    iH.checkForHeader(ind, line[:-1]) #removes the endl

dbg.c_settings() #DEBUGTOOLS

# Crop list so that i removes the header declarations
tokens = tokens[ind:]

#Check to make sure there's more than a header
if tokens[0] == '\end':
    exit("Error: No body present")



#Interpret the body
iB.init(doc)

for ind, line in enumerate(tokens):
    iB.parseLine(ind, line)


#SAVING AND WRITING THE DOCUMENT
dbg.c_void() #DEBUGTOOLS

if (ofile := _args.output) is None:
    doc.save(f'./{ofile[:-6]}docx')

else:
    if ".docx" in ofile:
        doc.save(f'{ofile}')
    else:
        exit("Error: Output file must have .docx extension")