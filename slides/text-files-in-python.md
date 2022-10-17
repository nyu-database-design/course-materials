---
layout: presentation
title: Text Files in Python
permalink: /slides/text-files-in-python/
---

class: center, middle

# Text Files in Python
Database Design

---

# Agenda

1. [Overview](#overview)
1. [Opening text files](#opening)
1. [Reading data from text files](#reading)
1. [Writing to text files](#writing)
1. [Character encoding issues](#encoding)
1. [Comma-Separated Values (CSV)](#csv)
1. [Javascript Object Notation (JSON)](#json)
1. [The pandas in the room](#pandas)
1. [HyperText Markup Language (HTML)](#html)
1. [Data Munging](#munging)
1. [Conclusions](#conclusions)

---

name: overview

# Overview

---

template: overview

## Intro
Python programmers use a variety of techniques for manipulating data in plain text files.  We will take a look at a few.

---

name: opening

# Opening text files

---

template: opening

## Modes of opening
A Pytyhon program can open a file in one of three modes:

--

- *read* - the program will be able to read data from the file

--

- *write* - the program will be able to completely overwrite the file's data

--

- *append* - the program will be able to add new data at the end of the file

--

It is possible to open a file in a combination of modes, but we will focus on each mode individually for simplicity.

---

template: opening

## open(...) function
Python's built-in `open()` function is the main tool for opening text files.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode
```

--

```python
f = open('amazing_data.txt', 'w') # open the file in write mode
# if the file does not yet exist, it will be automatically created
```

--

```python
f = open('amazing_data.txt', 'a') # open the file in append mode
# if the file does not yet exist, it will be automatically created
```

--

- In each of these examples, the variable, `f`, will refer to the file that has been opened.

--

- Further operations can be done on the data in the file through this `f` variable.

---

name: reading

# Reading data from text files

---

template: reading

## Basic concept
There are multiple ways to read data from a file in Python.  Which way you choose depends upon your needs.

--

- `f.read()` - returns the entire contents of the file as a *string*

--

- `f.readline()` - returns the next available single line of text (including the line break) as a *string*

--

- `f.readlines()` - returns a *list* containing all lines of the file as the values in the list

--

- *for loop* - can be used to iterate through the lines of a file

---

template: reading

## f.read()
Returns the entire contents of the file as a *string*.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode

all_text = f.read() # returns the entire contents of the file as a strings

# now do something fantastic and interesting with the data in all_text
```

---

template: reading

## f.readline()
Returns the next available single line of text (including the line break) as a *string*.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode

first_line = f.readline() # returns the first available line as a string (including line break)
second_line = f.readline() # returns the next available line as a string (including line break)
# ... and so on

# now do something fantastic and interesting with the data in first_line, second_line, etc.
```

--

Often, you want to remove the line break character from the end of each line.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode

first_line = f.readline() # returns the first available line as a string (including line break)
first_line = first_line.strip()

second_line = f.readline() # returns the next available line as a string (including line break)
second_line = second_line.strip()
# ... and so on
```

---

template: reading

## f.readlines()
Returns a *list* containing all lines of the file as the values in the list.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode

all_lines = f.readlines() # returns a *list* containing all lines of the file as the values in the list.

# now do something fantastic and interesting with the data in all_lines
```


---

template: reading

## for loops
It is possible to iterate through the lines of a file using a *for loop*.

--

```python
f = open('amazing_data.txt', 'r') # open the file in read mode

for line in f:
    line = line.strip() # remove the line break character

    # now do something fantastic and interesting with the data in line

```

--

- The loop will automatically terminate once it reaches the end of the file.

--

- This is often the easiest way to iterate through each line of a file and do something with it

---

name: writing

# Writing data to text files

---

template: writing

## Basic concept
Files can be either written from scratch or appended to, depending on whether the file is opened in *write* or *append* mode.

--

- `f = open('amazing_data.txt', 'w') # open the file in write mode`

--

- `f = open('amazing_data.txt', 'a') # open the file in append mode`

--

- In either mode, the `f.write()` function is used to write new text to the file.

--

- In either case, one *must* explicitly close the file with `f.close()` after writing to it.

---

template: writing

## Writing from scratch
In *write* mode, a file is created from scratch.  If the file already exists, it will be completely overwritten.

--

```python
f = open('amazing_data.txt', 'w') # open the file in write mode
```

--

```python
f.write("'Twas brillig, and the slithy toves")
f.write("Did gyre and gimble in the wabe:")
f.write("All mimsy were the borogoves,")
f.write("And the mome raths outgrabe.")
```

--

Close the file at the end.... *writing will not work without closing*.

--

```python
f.close() # close the file to finish the job
```
---

template: writing

## Appending
In *append* mode, an existing file is opened and added to.  If the file does not yet exist, it will be automatically created.

--

```python
f = open('amazing_data.txt', 'a') # open the file in append mode
```

--

```python
f.write('"Beware the Jabberwock, my son!')
f.write('The jaws that bite, the claws that catch!')
f.write('Beware the Jubjub bird, and shun')
f.write('The frumious Bandersnatch!"')
```

--

Close the file at the end.... *writing will not work without closing*.

--

```python
f.close() # close the file to finish the job
```

--

The file now contains the first two stanzas of Lewis Carroll's [Jabberwocky](https://en.wikipedia.org/wiki/Jabberwocky).

---

name: encoding

# Encoding issues

---

template: encoding

## Basic concept
Behind the scenes, plain text files contain only *ASCII* or *Unicode* codes, i.e. numbers in one of those encoding systems that represent characters.

--

- One day, you will open a file or web site that is supposed to show plain text. But you will see *garbled characters* and become confused.
```bash
ÉGÉìÉRÅ[ÉfÉBÉìÉOÇÕìÔÇµÇ≠Ç»Ç¢
```

--

- One day you will write a program that is supposed to open and read the contents of a file.  But it will *crash* and output something confusing about encodings.

--

- There is one explanation: *the program you have used to open the file is assuming the wrong encoding*.

---

template: encoding

## Determining a file's encoding
Determining a file's encoding can be a bit tricky, but there are a few common techniques.

--

- The UNIX `file` command can be used to guess the encoding in a given file, althought it's not always accurate, e.g. try `file somefile.txt` and see what is output.

--

- Most applications (editors, web browsers, etc) allow you to *select the encoding* in which to open the file.  Try a few until you find one that looks right!

--

- The Python module, `charade` is designed to help detect a file's character encoding. Running `charade.detect(some_string)` will return the proposed encoding as well as a confidence level between 0 and 1 on how sure `charade` is about its verdict.

--

Read more about the wonderful world of encodings [here](https://kunststube.net/encoding/).

---

template: encoding

## Dealing with encodings in Python

--

Python's default encoding when opening a file depends on the computer it's running on.

--

- *UTF-8*, one of several encodings in the *Unicode* standard, is often the encoding you want (but not always).

--

```python
f = open('amazing_data.txt', 'r', encoding='utf_8') # open in read mode with the common UTF-8 Unicode encoding
```

--

- See the full set of [character encodings supported by Python](https://docs.python.org/3.8/library/codecs.html#standard-encodings).

---

template: encoding

## A program's own encoding
Most computer programs are assumed to be written in ASCII.  However, you may want to include non-ASCII characters in your code.

--

- At the top of a program, you can indicate the encoding used by the code itself.

--

```python
# -*- coding: utf-8 -*-

# define a string with some non-ASCII characters... in this case Li Ba's poem, "Thoughts In Silent Night"
thoughts_in_silent_night = '''
李白《静夜思》
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''

# print out the poem
print(thoughts_in_silent_night)
```

---

name: csv

# Comma-Separated Values (CSV)

---

template: csv

## Basic concept
Python's [csv](https://docs.python.org/3/library/csv.html) module includes many functions useful for manipulating Comma-Separated Values (CSV) data.

---

template: csv

## Example
Take a CSV file, `nonsense.csv`, with famous nonsense literature works:

--

```csv
Last name,First name,Title,Year
Carroll,Lewis,Jabberwocky,1871
Lear,Edward,The Jumblies,1910
Bishop,Elizabeth,The Man-Moth,1946
```

--

Let's print out the title of each work using the `csv` module:

--

```python
import csv

f = open('nonsense.csv', 'r')
csv_reader = csv.DictReader(f)

for line in csv_reader:
    print( line["Title"] )

```

---

name: json

# Javascript Object Notation (JSON)

---

template: json

## Basic concept
Python's [json](https://docs.python.org/3/library/json.html) module includes many functions useful for manipulating Javascript Ojbect Notation (JSON) data.

---

template: json

## Example
Take a JSON file, `nonsense.json`, with famous nonsense literature works:

--

```json
[
    {"lastName": "Carroll", "firstName": "Lewis", "title": "Jaberwocky", "year": 1871},
    {"lastName": "Lear", "firstName": "Edward", "title": "The Jumblies", "year": 1910},
    {"lastName": "Bishop", "firstName": "Elizabeth", "title": "The Man-Moth", "year": 1946}
]
```

--

Let's print out the title of each work using the `json` module:

--

```python
import json

f = open('nonsense.json', 'r')
all_text = f.read() # get all text in file as a string

list_of_works = json.loads(all_text) # return a list of all works

# loop through each literature work
for work in list_of_works:
    print( work["title"] )
```

---

name: pandas

# The pandas in the room

--

## One module to rule them all
[pandas](https://pandas.pydata.org/) is an exceptionally powerful library for data analysis.

--

- It allows for easy reading of both CSV and JSON data files, as well as most other common formats.

--

```python
import pandas as pd
df = pd.read_csv('nonsense.csv') 
print( df['Title'] ) # output all titles
```

--

```python
import pandas as pd
df = pd.read_json('nonsense.json', orient='columns') 
print( df['title'] ) # output all titles
```

--

- pandas can do much more than this, but it cannot do everything.

---

name: html

# HyperText Markup Language

--

## Warning
While HyperText Markup Language (HTML) is one of the most common sources of loosely-structured and unstructured data today, it is *difficult to parse manually* due to its idiosyncratic syntax.

--

- Don't try to parse HTML manually... it's too much work.

--

- Use a readymade module such as [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) instead.

---

template: html

## Extraction with Beautiful Soup
Take, for example, the following HTML file named `nonsense.html`:

--

```html
<doctype html>
<html lang="en">
    <head>
        <title>Famous Works of Nonsense Literature</title>
    </head>
    <body>
        <section>
            <h1>Famous Works of Nonsense Literature</h1>
            <article>
                <h2>Jabberwocky</h2>
                <p>by Lewis Carroll<br />1871</p>
            </article>
            <article>
                <h2>The Jumblies</h2>
                <p>by Edward Lear<br />1910</p>
            </article>
            <article>
                <h2>The Man-Moth</h2>
                <p>by Elizabeth Bishop<br />1946</p>
            </article>
        </section>
    </body>
</html>
```

---

template: html

## Extraction with Beautiful Soup
The following Python program will *extract the titles* of each work of nonsense literature.

--

```python
from bs4 import BeautifulSoup

f = open('nonsense.html', 'r') # open the file in read mode
contents = f.read() # returns the entire contents of the file as a string
soup = BeautifulSoup(contents, 'lxml') # use Beautiful Soup to parse the html

# find all h1 tags and iterate through them
for tag in soup.find_all('h1'):

    # print out the contents of each h1 tag
    print( tag.text )
```

---

name: munging

# Data Munging

--

## Definition

> Data Wrangling, sometimes referred to as Data Munging, is the process of transforming and mapping data from one "raw" data form into another format with the intent of making it more appropriate and valuable for a variety of downstream purposes such as analytics. The goal of data wrangling is to assure quality and useful data. Data analysts typically spend the majority of their time in the process of data wrangling compared to the actual analysis of the data.
>
> -[Wikipedia](https://en.wikipedia.org/wiki/Data_wrangling)

--

- Pay special attention to that last sentence!

---

template: munging

## Common issues

While the meaning and values in data sets vary wildly from one to another, the issues a data analyst encounters when first trying to use the data are usually quite predictable.

--

- *determining the character encoding* - embarrassingly not as straightforward as one might expect

--

- *cleaning up data scraped from the web* - e.g. unescaping [html entities](http://www.entitycode.com/#common-content) and escape characters, removing html code altogether from the data

--

- *deciding what to do about missing values* - e.g. ignore them, invalidate the entire data series, fill them in with averages, etc

--

- *normalizing the data* - e.g. standardize capitalization and standardize the text used to indicate the same value, such as 'NYC' and 'New York City'

--

- *validating the data* - i.e. does it pass the *smell test* and seem to have reasonable values and the expected range of values in each field

---

name: conclusions

# Conclusions

--

Thank you.  Bye.
