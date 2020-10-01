import sys, os, json, argparse

from docx import Document
from docx.shared import Inches

from interpreters import interHeader as iH
from interpreters import interBody as iB

doc = Document()

#Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, metavar='ifile', help="input file, needs to have .pynote extension")
parser.add_argument("-o", "--output", type=str, metavar='ofile', help="output file, needs to have .docx extension")
parser.add_argument("-j", "--json", type=str, metavar='JSON', default="./configs/default.json", help="header JSON, default is ./configs/default.json")

args = parser.parse_args()

#Get the selected pynote file
if ".pynote" not in (ifile := args.input):
    exit("Error: Input file must have .pynote extension")

with open(args.input, "r") as f:
    textread = f.read()
tokens = textread.split()

#JSON Settings
with open(args.json, "r") as jsn:
    settings = json.load(jsn)

#I should have cmd line arg to add to another word doc

#Read Header
iH.init(settings)

for ind,word in enumerate(tokens):
    if iH.headerMode == False and iH.foundHeader == True: break
    iH.checkForHeader(ind, word)

settings = iH.settings

#SAVING AND WRITING THE DOCUMENT
if (ofile := args.output) == None:
    doc.save(f'./{ofile[:-6]}docx')

else:
    if ".docx" in ofile:
        doc.save(f'{ofile}')
    else:
        exit("Error: Output file must have .docx extension")

