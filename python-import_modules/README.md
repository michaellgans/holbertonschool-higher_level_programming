# Importing Modules

Hi there! :wave: <br>
These are the notes I took while working through this project. <br>
If you have questions, don't hesitate to reach out to me on slack! <br>

## Python vs C vs Bash

| Python | C | Bash |
|:-|:-|:-|
| Interpereted language | Compiled language | Not a programming Language |
| Easier to write | Requires more syntax | Simple to write |
| Comments: `/* this is a comment */` | Comments: `#this is a comment` | Comments: `#this is a comment` |
| Loop Syntax `for statement:` | Loop Syntax `for(statement) {` | N/A |
| If Syntax `if statement:` | If Syntax `if(statement) {` | N/A |
| Indicate code blocks with indents | Indicate code blocks with `{}` | N/A |
| and = `and` or = `or` | and = `&&` or = `\|\|` | N/A |
| Variables and their types are not declared | Variables and types are declared | N/A |
| Pointers aren't accessable | Pointers are accessable | N/A |
| Data structures are built in | Data structures are explicity stated | N/A |
| File extension `.py` | File extension `.c` | File extension `.txt` |
| Slower to run | Faster to run | Faster than Python |

## Importing Syntax

```
from module import function, function, function

if __name__ == "__main__":
  do action
  function() #to use a function
```
```
import module

if __name__ == "__main__":
  do action
  module.function() #to use a function
```

### Resources
https://www.geeksforgeeks.org/difference-between-c-and-python/ <br>
https://www.geeksforgeeks.org/difference-between-python-and-bash/ <br>
https://markdown.land/markdown-table <br>
