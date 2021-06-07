# file-inspection-evasion-PoC
Implementation of an antivirus evasion technique to hide files in Zip archives

## General Info
This implements three antivirus evasion technique for zip files

The three different techniques to choose from are Ghost File,
Invalid File Header, and File Buffers Collapsing.

Technique One Ghost File:
Removes the central directory from the zip file so it can't be used to index
the archive contents.

Technique Two Invalid File Header:
Adds an invalid header to the beginning of the file to prevent the archive
from being indexed based on the local file headers.

Technique Three File Buffer Collapsing:
Adds a file at the beginning of the archive with an edited file size to
engulf any other files in the archive to prevent indexing of the files from
the local file headers.

The newly created file will be placed in the same directory as the original with
a file name prefixed with flags_ and the what flag was provided. 
Example: flags_g_files.zip

It is possible to chain multiple techniques together but depending one which 
ones that could complicate recovering the files after.

## Usage
### Command line examples:

There is a command line interface for this tool

Run the Ghost technique on the file 
```
$ python main.py -f test_files/files.zip -g
```

Run the Invalid Header technique on the file 
```
$ python main.py -f test_files/files.zip -i
```

Use in another project
```python
import exploit.file_inspection_evasion as fie

technique = ['ghost']
file_loc = test_files/files.zip

fie.evade(file_loc=file_loc, techniques=technique)
```

run test from home dir with
```
$ python -m unittest
```

