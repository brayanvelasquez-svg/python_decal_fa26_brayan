# homework5.py



# 2.1 Vocabulary Review

# Git vs GitHub - Git tracks coding locally while GitHub is where code can be uploaded into a cloud-like system and you can work on coding remotely.

# Terminal vs Command Line - Terminal is where all the results of your code appears after you run it and the command line is where you write the actual code.

# Local vs Remote Repository - Local only allows you to work on that code on a specific computer/laptop while Remote lets you work on it from any computer.

# Version Control - It is what allows python to keep track of all the changes being made within the coding.

# Staging Area - It is a place where your files are waiting to be saved and then pushed.

# git add - This is the command that adds files and starts the process of being transferred into a remote repository.

# git commit - This is when files are saved and are awaiting to be added to the remote repository, waiting in the staging area.

# git push - This is when the files are officially sent to the remote repository.

# git status - Tells us the status of our code and whether or not something is being saved or has an error.

# git pull - A combination of git fetch and git merge that allows updates from the remote repository to merge with the local branch.

# pwd - Shows the full path of the directory you are currently in.

# ls - Lists all of the content inside of the directory you're in.

# cd - Allows you to move from directory to directory.

# nano - Allows you to open a python file and edit it (like this one!).

# touch - Allows you to create a python file.

# mv - Can change the name or location of a file/directory.

# rm - Deletes files or directories.

# cat - Displays the file contents.



# 2.2 A Directory Tree

# pwd

# ls

# git pull

# mv homework.py homework/

# cd .. then cd judy_decal then cd homework

# cat homework.py

# git add . then git commit -m then commit push

# git status and the error means that you need to update first

# ~/Recents/ (I'm not sure if we are starting from the beginning so I will assume we are)

# 3.1 Data Types
def checkDataType(data):
    if isinstance(data, int):
        return "Integer"
    elif isinstance(data, float):
        return "Float"
    elif isinstance(data, str):
        return "String"
    elif isinstance(data, list):
        return "List"
    elif isinstance(data, dict):
        return "Dictionary"
    elif isinstance(data, bool):
        return "Bool"
    else:
        return "Unknown data type"
print(checkDataType(3.14))
print(checkDataType(True))
print(checkDataType("Hello"))
print(checkDataType([1, 2, 3]))
print(checkDataType({"Katy Perry": "Singer", "Katseye": "Singer"}))

# 3.2 Conditionals
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(4))
print(evenOrOdd(7))
print(evenOrOdd(143))

# 4 Loops
def sumWithLoop(lst):
    total = 0
    for num in lst:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# 5.1 Lists
def duplicateList(lst):
    duplicated = []
    for item in lst:
        duplicated.extend([item, item])
    return duplicated
print(duplicateList([3, 5, 7]))

# 5.2 Debugging
def square(num): # The colon was missing at the end of the function definition, which is necessary to define a function in Python.
    return num * num
print(square(5))

# Favorite Function
# def duplicateList(lst):
#     duplicated = []
#     for item in lst:
#         duplicated.extend([item, item])
#     return duplicated
print(duplicateList([143, 94384, 79349287]))