import sys, os, json
from docx import Document
from docx.shared import Inches

from interpreters import interHeader as iH
from interpreters import interBody as iB

doc = Document()

#Get the selected pynote file
filearg = sys.argv[1]

with open(filearg) as f:
    textread = f.read()
tokens = textread.split()

#JSON Settings
defaultarg = sys.argv[2]

if defaultarg == 'd': defaultarg = './configs/default.json'
with open(defaultarg) as jsn:
    settings = json.load(jsn)

#Read Header
iH.init(settings)

for ind,word in enumerate(tokens):
    if iH.headerMode == False and iH.foundHeader == True: break
    iH.checkForHeader(ind, word)

settings = iH.settings

#SAVING AND WRITING THE DOCUMENT
exportarg = sys.argv[3]

if ".docx" in exportarg:
    doc.save(f'{exportarg}')
else:
    doc.save(f'{exportarg}/{filearg[:-6]}docx')
