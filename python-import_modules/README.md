# Importing Modules

Hi there! :wave: <br>
These are the notes I took while working through this project. <br>
If you have questions, don't hesitate to reach out to me on slack! <br>

## Python vs C
The following are differences between Python and C

### C
- Compiled Language
  - Needs to be compiled with GCC.
- Syntax Heavy
- Comments: */ this is a comment */
- ; after loops
- If syntax `if(), else if(), else()`
- Use `{}` to show code blocks
- and = &&
- or = ||
- Variables are declared and type is declared`char c;`
- Pointers are accessable
- Data structures are explicitly stated
- `.c` extension
- Faster than Python

### Python
- Interpreted Language
- Comments `#thisisacomment`
- : after loops
- If syntax `if, elif, else :`
- No curly braces to show code blocks
- and = and :smile:
- or = or
- Object Oriented
- Variables or type of variable is not declared `c = 10`
- Pointers are not accessable
- Data structures are built in
- `.py` extension
- Slower than C because it compiles for you
  - Needs an interpereter!

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
https://www.geeksforgeeks.org/difference-between-c-and-python/
