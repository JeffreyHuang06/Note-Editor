# from docx import Document
# from docx.shared import Inches

# doc = Document()
# r1 = doc.add_paragraph("hello")
# run = r1.add_run("hi")
# run.bold = True
# f = run.font
# f.highlight_color = 7

# doc.save("test.docx")
# import os
# print(os.path.dirname(os.path.realpath(__file__)))

# import t2
#
# x=  [5]
# t2.test(x)
# print(x)

import builtins

def mt():
    print("hello world")

builtins.mytest = mt

mytest()