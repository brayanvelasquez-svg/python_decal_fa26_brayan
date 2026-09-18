# File: homework1.py

# --- Variables and Data Types ---
a = 10
print (a)
print (type(a)) # a is an integer
b = 1.5
print (b)
print (type(b)) # b is a float
c = 3j
print (c)
print (type(c)) # c is a complex number
d = "hello"
print (d)
print (type(d)) # d is a string
e = [1, 2, 3]
print (e)
print (type(e)) # e is a list
f = {"name": "Brayan", "favorite fruit": "pineapple"}
print (f)
print (type(f)) # f is a dictionary
g = (1, 2)
print (g)
print (type(g)) # g is a tuple
h = ["apple", "banana", "strawberry"]
print (h)
print (type(h)) # h is a list
i = True
print (i)
print (type(i)) # i is a boolean
j = None
print (j)
print (type(j)) # j is a NoneType
k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list
l = str(14)
print (l)
print (type(l)) # l is a string
m = 1e4
print (m)
print (type(m)) # m is a float
# Question 1: I found 9 different data types.
# Question 2: The data types I found are: integer, float, complex number, string, list, dictionary, tuple, boolean, and NoneType.
# Question 3: The variables that have the same data type are e, h, and k (all lists), d and l (both strings), and b and m (both floats).
# Question 4: The data type of l is a string. It is not an integer because it was created using str(). What str() does is convert any value into a string.
# Question 5: One more data type that isn't listed above is a set. 
n = {1, 2, 3}
print (n)
print (type(n)) # n is a set

# --- Booleans ---
print (10 > 9) # True, 10 is greater than 9
print (10 == 9) # False, 10 is not equal to 9
print (10 <= 9) # False, 10 is not less than or equal to 9
print (bool ("abc")) # True, "abc" is a non-empty string
print (bool(123)) # True, 123 is a non-zero number
print (bool(["apple", "cherry", "banana"])) # True, the list is not empty
print (bool(True)) # True, the value is True
print (bool(False)) # False, the value is False
print (bool(0)) # False, 0 is considered False
print (bool("")) # False, an empty string is considered False
print (bool(" ")) # True, a string with a space is considered True
print (bool(())) # False, an empty tuple is considered False
print (bool([])) # False, an empty list is considered False
print (bool({})) # False, an empty dictionary is considered False
print (bool(True and False)) # False, True and False evaluates to False
print (bool(True and True)) # True, True and True evaluates to True
print (bool(False and False)) # False, False and False evaluates to False
print (bool(True or False)) # True, True or False evaluates to True
print (bool(True or True)) # True, True or True evaluates to True
print (bool(False or False)) # False, False or False evaluates to False
print (bool(not (False))) # True, not False evaluates to True
print (bool(not (True))) # False, not True evaluates to False
# Question 1: The pattern I noticed about expressions returning True or False is that expressions with "and" return True only if both operands are True, while expressions with "or" return True if at least one operand is True. The "not" operator negates the boolean value of the expression it precedes.
# Question 2: The expression that surprised me was bool(" "), which returned True. I expected it to return False because it is a string with only a space, but in Python, any non-empty string is considered True.
# Question 3: print (bool(not (not True))) returns True. It returns True because the first "not" negates True to False, and the second "not" negates False back to True.
# Question 4: print (bool(not (not (not True)))) returns False. It returns False because the innermost "not" negates True to False, the next "not" negates False back to True, and the outermost "not" negates True to False.

# --- Operators ---
# --- Arithmetic Operators ---
print (10 + 5) # 15, + performs addition
print (10 - 5) # 5, - performs subtraction
print (2 * 4) # 8, * performs multiplication
print (6 / 3) # 2.0, / performs division
print (5 % 2) # 1, % performs modulus (remainder of division)
print (3 ** 2) # 9, ** performs exponentiation (3 raised to the power of 2)
print (15 // 2) # 7, // performs floor division (division that rounds down to the nearest whole number)
# --- Comparison Operators ---
print (5 == 2) # False, 5 is not equal to 2
print (10 != 10) # False, 10 is equal to 10
print (2 > 5) # False, 2 is not greater than 5
print (12 > 5) # True, 12 is greater than 5
print (5 <= 6) # True, 5 is less than or equal to 6
print (1 >= 10) # False, 1 is not greater than or equal to 10
# --- Assignment Operators ---
x = 5
x += 5 # x is now 10, += adds the right operand to the left operand and assigns the result to the left operand
x -= 4 # x is now 1, -= subtracts the right operand from the left operand and assigns the result to the left operand
x *= 3 # x is now 15, *= multiplies the left operand by the right operand and assigns the result to the left operand
# --- Logical Operators ---
# Question 1: The operator "and" returns True only if both operands are True. print (True and True) # True. print (True and False) # False.
# Question 2: The operator "or" returns True if at least one operand is True. print (True or False) # True. print (False or False) # False.
# Question 3: The operator "not" negates the boolean value of the operand. print (not False) # True. print (not True) # False.
# More Questions:
# Question 1: The difference between / and // is that / performs regular division and returns a float, while // performs floor division and returns the largest integer less than or equal to the result.
# Question 2: The difference between % and // is that % returns the remainder of the division, while // returns the quotient rounded down to the nearest whole number.
# Question 3: The operator used to calculate the remainder when dividing two numbers is the modulus operator %, which returns the remainder of the division. print (10 % 3) # 1, because 10 divided by 3 is 3 with a remainder of 1.
# Question 4: Assignment operators work by taking the current value of a variable, performing an operation with another value, and then assigning the result back to the variable. For example, x += 5 takes the current value of x, adds 5 to it, and assigns the result back to x.

# --- Strings ---
my_string = "hello"
print (my_string) # hello
print (my_string[0]) # h, accessing the first character of the string
print (my_string[1]) # e, accessing the second character of the string
print (my_string[2]) # l, accessing the third character of the string
print (my_string[3]) # l, accessing the fourth character of the string
print (my_string[4]) # o, accessing the fifth character of the string
print (my_string[-1]) # o, accessing the last character of the string using negative indexing
print (my_string[1:3]) # el, slicing the string from index 1 to 3 (not including index 3)
print (my_string[0:5:2]) # hlo, slicing the string from index 0 to 5 with a step of 2
print (len(my_string)) # 5, getting the length of the string
print (my_string + "goodbye") # hellogoodbye, concatenating two strings
print (my_string * 7) # hellohellohello, repeating the string 7 times
# Question 1: The term slicing means extracting a portion of a string (or other sequence types) by specifying a start index, an end index, and an optional step. The manipulations that I sliced my string were: my_string[1:3] which extracted "el" from "hello", and my_string[0:5:2] which extracted "hlo" from "hello".
# Question 2:
name = "Oski"
print ("Hello, my name is", name)
# The result is that "Oski" replaced name in the string.
# Question 3:
name = "Oski"
print (f"Hello, my name is {name}")
# The result is the same as the previous question, resulting in "Oski" replacing {name} in the string.
# Question 4: The difference between the two strings is that the first one uses string concatenation with a comma, which adds a space between the strings, while the second one uses an f-string, which allows for inline variable substitution without adding extra spaces. The output of the first one is "Hello, my name is Oski" and the output of the second one is also "Hello, my name is Oski", but they are constructed differently.

# --- Terminal Commands ---
'''
cd
cd changes directory. Use it to move between folders.
Example: cd homework1
ls
ls lists the items of the directory you're in. Use it to see what files and folders are in that directory.
Example: ls
ls -a
ls -a lists all items of the directory you're in, including hidden files. Use it to see everything in that directory.
Example: ls -a
mkdir
mkdir creates a new directory. Use it to make a new folder.
Example: mkdir new_folder
cat
cat shows the contents of a file. Use it to read the contents of that file.
Example: cat homework1.py
pwd
pwd prints the current working directory. Use it to see where you are in the file system.
Example: pwd
cd ..
cd .. moves you up one directory level. Use it to go back to the parent directory.
Example: cd ..
cd .
cd . keeps you in the current directory. Use it to stay in the same folder.
Example: cd .
cd ~
cd ~ takes you to your home directory. Use it to quickly return to your home folder.
Example: cd ~
cp 
cp copies files or directories. Use it to duplicate files or folders.
Example: cp homework1.py homework1_copy.py
mv
mv moves or renames files or directories. Use it to change the location or name of a file or folder.
Example: mv homework1.py homework1_thatiamdoingatmidnight.py
rm
rm removes files or directories. Use it to delete files or folders.
Example: rm homework1_copy.py
clear
clear clears the terminal screen. Use it to remove all previous commands and outputs from view.
Example: clear
grep
grep searches for a specific pattern in files. Use it to find lines with a certain string.
Example: grep "hello" homework1.py
'''
# Question 1: 3 other commands that are not present are: touch, which creates a new empty file; rmdir, which removes an empty directory; and echo, which displays a line of text or a variable value in the terminal.
# Question 2: The difference between ls and ls -a is that ls lists only the visible files and directories in the current directory, while ls -a also lists hidden ones (those starting with a dot).
# Question 3: A hidden file is a file that is not normally visible when listing the contents of a directory. They normally start with a dot (.).
# Question 4: 3 other flags are -l, which lists files in long format with detailed information; -h, which makes file sizes human-readable; and -R, which lists files recursively in all subdirectories. The way you use them on the command line is by connecting them to a command, for example: ls -l, ls -h, or ls -R.