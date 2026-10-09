# 3 - Lists

# 3.1 List Operations
fav_food = ["sushi", "burger", "pasta", "pupusa", "korean corn dogs"]
print(fav_food[1])
print(fav_food[-1])
fav_food.append("terryaki chicken")
print(fav_food)
fav_food[0] = "apple"
print(fav_food)
print(len(fav_food))
words = fav_food 
uppercase_words = [w.upper() for w in words]
print(uppercase_words)
"""
I encountered this error:
AttributeError: 'list' object has no attribute 'upper'
I originally wrote:
print(fav_food.upper())
I did not format this correctly. What I did to fix it was search online how to apply .upper() to a list and it told me I had to set my list equal to words. Then I made a new string called uppercase_words and set it to the correct format I saw online, resolving my problem!
"""
sub_fav_food = fav_food[0::5]
print(sub_fav_food)
def potato(fav_food):
	if "potato" in fav_food:
		"""
		I encountered this error:
		"IndentationError: expected an indented block after function definition on line 12"
		I originally wrote:
		if "potato in fav_food:"
		I forgot to indent. I fixed it by indenting.
		"""
		return "A potato!"
	else:
		return "No potato..."
print(potato(fav_food))

# 3.2 Slicing and Striding
numbers = range(0, 21)
def get_first_15(numbers):
	"""
	I encountered this error:
	NameError: name 'get_first_15' is not defined
	I originally wrote:
	get_first_15(numbers)
	I assumed get_first_15 would work on its own for some reason. I fixed it by defining it and returning the list of numbers
	"""
	return (list(numbers[0:16]))
print(get_first_15(numbers))


get_first_15 = (list(numbers[0:16]))
def get_every_5th(get_first_15):
	return (list(get_first_15[::5]))
print(get_every_5th(get_first_15))

get_every_5th = (list(get_first_15[::5]))
def reverse_and_stride(get_every_5th):
	return (list(get_every_5th[::-3]))
print(reverse_and_stride(get_every_5th))

# 3.3 Nested List
number_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(number_list[2])
print(number_list[1][1])
number_list.append([10, 11, 12])
print(number_list)

# 3.4 Create a 5x5 List
def nested_loops():
    fivexfive_list = [] # Starts an empty lisy
    for i in range(5): # Creates the 5 rows
        row = [] # Starts an empty list for each row
        for j in range(5): # Creates the 5 numbers in each row
            row.append(i * 5 + j + 1) # Adds the numbers 1 to 25
        fivexfive_list.append(row)
    return fivexfive_list
fivexfive_list = nested_loops()
print(fivexfive_list)

def replace_multiples(fivexfive_list):
	for i in range(5): 
		for j in range(5): # The last 2 commands go through every single position in the 5x5 list.
			if fivexfive_list[i][j] % 3 == 0: # i represents what row, j represents what value in that row, and the math is referring to any integers when divided by 3 = 0.
				fivexfive_list[i][j] = "?" # If a number is divisible by 3, replace it with "?"
	return fivexfive_list
updated_list = replace_multiples(fivexfive_list) 
print(updated_list)

def add_numbers(updated_list):
	total = 0

	for i in range(5):
		for j in range(5):
			if updated_list[i][j] != "?": # != means "not equal to", so "?" != "?" is false and gets skipped.
				total += updated_list[i][j] # Adds current number to total.
	return total
sum_result = add_numbers(updated_list)
print(sum_result)
# 4.1 Dictionary Operations
ages = {
	"Katie": 30,
	"Mariam": 42,
	"Safia": 25,
	"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
print(ages)
ages["Milana"] = 52
print(ages)
del ages["Mariam"]
print(ages)
for name, age in ages.items():
	print(name, age)
	