# holbertonschool-higher_level_programming

## New_File

```
#!/bin/bash

#prompts user for new file name
printf "New File Name:\t"

#sets M as variable for input
read M

#write the first line of the new file
echo "#!/usr/bin/python3" > "$M"

#makes new file executable
chmod u+x "$M"

#opens new file
vi "$M"
```

## Push

```
#!/bin/bash
printf "Commit Message:\t"
read M
git add .
git commit -m "$M"
git push
```

## How to use the `print()` statement:

>- General Use: `print("This will print!")
>- Quotes: single vs double doesn't matter, just make them match.
>- Special Character Escaping: use `\` to ensure a special character is printed.
>- Printing Varaibles: `print(VAR)` works just fine

## How to pass a variable into a print statement:

>- Remember to use `print(f"The variable is: {VAR}")` when passing in a variable like a number 😉

## How to format data inside a print statement:

>- There are two different ways to do this, but it's typically referred to as f-string formatting.
>- the `.2` indicates that you want two decimal places and the `f` indicates that the data type is float.
```
print(f"{VAR:.2f}")
```
