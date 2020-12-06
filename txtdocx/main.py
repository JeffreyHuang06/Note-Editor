#transfers it from txt, therefore no tags
import typing, argparse
from docx import Document 
from docx.shared import Inches

from src.args import _args
from src.settings import _settings

from utils import debugtools as dbg

#make the document
doc = Document()

#open the document
text=''
with open(_args.input, "r+") as fin:
    text = fin.read()

#add the text
par = doc.add_paragraph(text)

dbg.c_void() #DEBUGTOOLS

if (ofile := _args.output) == None:
    doc.save(f'{_args.input[:-4]}.docx')

else:
    if ".docx" in ofile:
        doc.save(f'{ofile}')
    else:
        exit("Error: Output file must have .docx extension")

exit()
