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

# For the read-me-pros!

## Lists
#### Block Lists
>- Your text here
>- Your text here

#### Lists/Sub-Lists
- Your text here
  - Your text here
- Your text here

## Tables
Title | Of | Your | Table
:--|:--:|--:|--
Right aligned | Center aligned | Left aligned | Default
Your text here | Your text here | Your text here | Your text here
Your text here | Your text here | Your text here | Your text here
