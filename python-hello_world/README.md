# Python-Hello_World
Hello everyone! <br>
These are the notes I've taken while doing this project.  
Please don't hesitate to reach out if you need assistance.

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

## How to print a specific number of characters:

>- Keep in mind that this is a zero based index.
>- You can access a range of characters by using `[start:stop]`
```
print(VAR[0:4])
```
This would print the first FIVE characters of what is stored inside of VAR.

## How to concat in python:

>- To join two variables together, use `+`.
>- Play around with the spacing.

```
str1 = "Apples"
str2 = "Bananas"
str1 = str1 + str2
print(f"Output: {str1}")
```
Output: ApplesBananas

```
str1 = "Apples"
str2 = "Bananas"
str1 = str1 + " " + str2
print(f"Output: {str1}")
```
Output: Apples Bananas
