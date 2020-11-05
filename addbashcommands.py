import os, platform
pathname = os.path.dirname(os.path.realpath(__file__))

currentplatform = platform.system()

if "darwin" in currentplatform:
    with open("~/.bash_profile","a+") as f:
        newstr = "\npython3(){\ntxt2docx " + f"{pathname}/main.py $1" + "}\n"
        f.write(newstr)

if "win" in currentplatform:
    with open("~/.bash_profile","a+") as f:
        newstr = "\npython(){\ntxt2docx " + f"{pathname}/main.py $1" + "}\n"
        f.write(newstr)

else:
    raise "Unsupported platform. Only Mac and Windows supported"