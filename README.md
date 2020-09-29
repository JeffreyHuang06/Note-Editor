# pynote
.pynote
A note taking markup language, using the guide in Docs.pynote or in this readme.
Use the python file in terminal to convert to word doc
Reduces time having to fiddle with the buttons on Microsoft Word

## Setup
Requires at least Python 3.8
```bash
pip install -r requirements.txt
```

## Covert to .docx
### MacOS
```bash
python3 main.py [filename] [config json]
```
Examples:
```bash
python3 main.py historynotes.pynote d
python3 main.py historynotes.pynote myPersonalConfig.json
```
The default configuration JSON is in ./configs/default.json where you can jsut specify the path with "d"

### Windows
```bash
python main.py [filename] [config json]
```
Examples:
```bash
python main.py historynotes.pynote d
python main.py historynotes.pynote myPersonalConfig.json
```
The default configuration JSON is in ./configs/default.json where you can jsut specify the path with "d"

## Documentation
