# holbertonschool-higher_level_programming

This is an update at 4:45 PM.

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
