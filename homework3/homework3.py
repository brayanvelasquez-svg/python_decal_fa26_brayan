# name = "Brayan"

# print ("Hello", name)

# def say_goodbye(name):
#     print("Goodbye", name)

# say_goodbye(name = "Brayan")

radius = 5

def circle_area(a, b):
    print(a * b)
print(circle_area(3.14, 5**2))

def subtract(a, b):
    return a - b

print(subtract(1432, 143))

def multiply(a, b):
    return a * b

print(multiply(14, 3))

def divide(a, b):
    return a / b

print(divide(1432, 2))

List = [60, 67, 69, 75, 71, 80, 89, 143]

def tuple_list(List):
    return ((min(List)), (max(List)))

print (tuple_list(List))

1 == "Monday"

2 == "Tuesday"

3 == "Wednesday" 

4 == "Thursday" 

5 == "Friday" 

6 == "Saturday"

7 == "Sunday"

def is_weekend(int):
    if int == 6 or int == 7:
        return "True!"
    else:
        return "False..."

print (is_weekend(7))

def fuel_efficiency(distance, fuel):
    mpg = distance / fuel
    return mpg

print(fuel_efficiency(100, 10))

def encrypt(number):
    last_digit = number % 10 # Modulus gives the remainder
    remaining = number // 10 # Removes the decimal portion
    text = str(last_digit)
    text = str(remaining)
    result = str(last_digit) + str(remaining) # Adds them as strings and not as integers to combine them
    return result

print(encrypt(14325))

def power(x, y):
    result = 1 # Multplying by 1 leaves number unchanged
    for i in range(y):
        result *= x # Depending on y, the loop runs that amount of times
        
    return result

print(power(5, 3))

def find_min(numbers):
    smallest = numbers[0] # Starts counting list positions, in this case it starts with 7

    for number in numbers: # loop takes one number at a time
        if number < smallest:
            smallest = number # compares current number to smallest found so far
    return smallest

print(find_min([7, 1, 4, 3, 2]))

def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number # compares current number to biggest found so far
    return largest

print(find_max([7, 1, 4, 3, 2]))

def find_min_while(numbers):
    smallest = numbers[0] 
    i = 1 # Counter starts at 1 because 0 is already used

    while i < len(numbers): # Gives number of items in the list
        if numbers[i] < smallest:
            smallest = numbers[i]

        i += 1 # Without this, i would never change and would loop forever
    return smallest

print(find_min_while([7, 1, 4, 3, 2]))

def find_max_while(numbers):
    largest = numbers[0]
    i = 1

    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]

        i += 1
    return largest

print(find_max_while([7, 1, 4, 3, 2]))

def sum_digits(number):
    total = 0 # Start at 0 becauseno digits added yet

    while number > 0:
        digit = number % 10 # last digit is collected
        total += digit # digit is now being added to total
        number //= 10 # cuts the number down one integer, starting the next number to be collected

    return total

print(sum_digits(1432))

number = 37122781
result = sum_digits(number) # all integers added to each other

print(f"The result of Calculate the Sum (6.3) with number = {number} is {result}.")