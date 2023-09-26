# Input/Output

## SYSK

How to open a file
- You can open a file using the `open()` function
    - `r` - read only permissions
    - `r+` - read and write permissions
    - `a+` - append and read permissions
How to write text in a file
How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure
How to access command line parameters in a Python script

## FYSK

Syntax | Notes
--- | ---
`file_object = open("File_name", "permissions")` | put an r at the beginning of the string if the file name isn't in the same directory.
`file_object.close()` | to close a file when you're finished
`file_object.read([n])` | to read from a file where n is the bytes of data.  if you leave it blank, it reads the whole file.
`file_object.readlines()` | reads all the lines and returns them as a list of elements
