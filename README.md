# pyNote
A note taking markup language, using the guide in Docs.pynote or in this README  
Use the python file in terminal to convert to word doc  
Reduces time having to fiddle with the buttons on Microsoft Word  

## Setup
Requires at least Python 3.8
### MacOS
```bash
pip3 install -r requirements.txt
```

# Windows
```bash
pip install -r requirements.txt
```

## Covert to .docx
### MacOS
```bash
python3 main.py [input file]
```
Examples:
```bash
python3 main.py historynotes.pynote d
python3 main.py historynotes.pynote --json myPersonalConfig.json
python3 main.py historynotes.pynote --json myOtherConfig.json --output notes.docx
```
<br>
For more information on the command line arguments, do

```bash
python3 main.py --help
```

### Windows
```bash
python main.py [input file]
```
Examples:
```bash
python main.py historynotes.pynote d
python main.py historynotes.pynote --json myPersonalConfig.json
python main.py historynotes.pynote --json myOtherConfig.json --output notes.docx
```
<br>
For more information on the command line arguments, do

```bash
python main.py --help
```

## Documentation
### Size Markers
##### `\h` - Heading
##### `\t` - Topic
##### `\r` - Regular Chunk  
<br>
Size markers can also be extended to different numerical subtypes

##### `4\h` - Heading - Type 4
##### `2\t` - Topic - Type 2
##### `1\r` - Regular Chunk - Type 1
<br>
These, however will lead to an error

##### `0\h` - Only positive integer subtypes
##### `a\t` - Can only be numerical
<br>
You can assign the font size inline when using a Size Marker

##### `\h=28` - Heading - Size 28
##### `4\t=15` - Topic - Type 4 - Size 15
##### `1\r=11` - Regular Chunk - Type 1 - Size 11

#### Notes:
The Regular Chunk does not self close, it has to be represented like

##### ```\r Text \\r```
and likewise with the subtypes

##### ```4\r=12 Text 4\\r``` - Regular Chunk - Type 4 - Size 12

### Styles
##### `\b` - Bold
##### `\i` - Italics
##### `\q` - Quotes
##### `\l` - Highlights
<br>
These close like Size Markers

##### ```\b Text \\b```
<br>
There is another Style which doesn't behave the exact same way

##### `i[]` - Emphasis
Which can be used like

##### `i[Text]` - "Text" is emphasized
You can program Emphasis in the Header
<br>
All 5 Styles can be nested

##### ```\q \b \i Lorem \\i Ipsum \l Dolor \\l i[\b sit \\b] \q amet``` 

#### Notes:
The Quote can be mixed and matched with the actual character too, although this can make conversion quite slow, so this option can be turned off in the Header. The quote also does not close the same way as the other styles
Something like this will work
```
\q Hello \q
"Hello \q
\q Hello"
```
This mixing and matching is called Indeterminate-Quote

### Advanced Size Markers and Styles
To make an entire singular line a style or size, you can just put an ending without the beginning
```
This will all be bold \\b
This will \\b partly be bold and 14pt 1\\h=14
This line will be quoted \\q
This will be emphasized and italicised \\i \\i[]
```
Emphasis can be multilined
```
I[
    all is emph
    hi
]
```

### Variables
Variables can store text which can then be placed in later
```
\v=Aztec
\v 
\v
\v
The word \v has been pasted 4 times
```
<br>
Variables can also be subtyped

```
1\v=Hi
a\v=Aztec
90\v=Hello
```
<br>
Spaces exist via braces or underscores

```
\v={The Aztecs}
\v
\v
\v
\v had been decimated by Spanish Conquistadores in the 16th centuty
```
<br>
Whole lines can be declared with a double backslash variable declaration

```
This is all a var \\v=
i can paste it here : \v
```
<br>
A powerful functionality is that they can store whole styles and sizes

```
1\v={\b \t}
2\v=\\b
1\v Text 2\v
Only bold \\v 
```
When a corresponding size changes, the variable changes
```
\t=5 This is size 5
\v=\t This is size 5
!\t=6
\v This is now size 6
```

### Unpure-Text
This encompasses everything which isn't pure text, like bullets and dates, and also tabs
#### Tabs or Indents
Tabs and Indents can be expressed as tags,
and Indents can be multiline
```
\ind indented
\tab
this
is 
all 
tabbed
\\tab
```

#### Bullets
These can be marked in currently only one way
```
\bull
- Hello
-- Double Hello
-- \t Hi
-*4 This is ranked 4
\
```
Bullets are ended by a single backslash
If you don't like multiplication in your indents, use the ind tag
```
\bull
- hi
\tab
hi
hi
\tab
hello
\\tab
\\tab
\  
```

You can also remove the space, but this is called Indeterminate-Bullets, which can be toggled in the heading
<br>  

``` 
\bull
-HI
-hi
-these dont have spaces
- but this does
\  
```

### Special Keywords
There are special key words that can als be used.
#### Auto
This automatically applies the size or style to any text.
```
\t=5\auto=Hi
```
It can be declared in a heading

### Temps, Overwrites, Size Inheritance, and Invisibility
#### Temporary Declarations
For the Size Markers, you can put a tilde before them to make them only last for one line.
```
\h=6 This is size 6
~\h=2 This is size 2
But this is size 6
```
```
~\b This is only bold for this line
1\t=2 This is size 1
~1\t=15 But this is size 15
1\t Although this is back to normal
```
You don't need a backslash to make it temporary.

#### Overwrites
Sometimes you just to clear everything and go back to the default, use the plain tag
```
\plain{{
    text goes here
}}
```
No tags will be registered in here, unless you use the esc tag
```
\plain{{

    this is written with the backslash \h \\ \ \\q
    \esc{{ \h but this isnt }}
}}
```
<br>
If you want to make an entire section a style and size, you can use the div tag

```
\div \h=5 \l 
    All 
    these
    lines
    are 
    size 5
    and
    highlighted
\\div
```
Note that the indents are not necessary.

#### Size Inheritance
Like variables, sizes can inherit from other sizes
```
1\t=5
\h=1\t This is also a header and size 5

\h=1\t*3 This is size 15
\h=1\t+2 This is size 7
1\t=6
\h This is size 8
```

#### Invisibility
You can see in declarations you have to use them, but with an exclamation mark, you can simply declare without use.
```
!\h=5
\h This wont error

!\h=5 !\1\t=19
that won't error ^^^

!\h=2 However this will
```

### Tag Order
The tag order is as follows
```
~3\h=1\t+3 or !3\h=1\t+3
[~,!,][subtype]\[size]=[tag,number][modulator]
```
For sizes, it goes whether inv, temp, or none.
Then you have your subtype.
Then you have your size type.
Then you hace either a size or an inheritance from another tag

For variables, the order is as follows
```
[~,!,][subtype]\v=[{},text,style,size]
```
First it goes inv, temp, or none.
Then subtype.
Then \v=
Then you can either use a combination, a word, a style, or a size type.

### The Header
The Header is one of the most important parts of a pyNote.  
Although optional, which if you don't include it, it goes to the default config  
In the Header, it can rewrite rules and sizes
It is denoted by

```
\header
\end
```

<br>
In the header, you don't need backslashes
An example is

```
\header
h=12
t=5
r=3
size=2
v={\b \t}
Indeterminate-Quote=False
Indeterminate-Bullet=False
Inline-Style=False
\end
```

The size parameter is Header specific, you cannot declare it outside the Header
You can also observe that you can't declare subtypes, but you can declare them in the config JSON

### Coming Soon - Code Markup
`\if{\t=1}!\t=5` - if Topic Size = 1, then Topic Size = 5
