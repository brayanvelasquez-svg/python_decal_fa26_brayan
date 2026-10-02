# name = "Brayan"

#  print ("Hello", name)

# def say_hello(name):
#     print("Hello", name)

# say_hello(name)
# say_hello(name="Brayan")

# def add(a,b):
#     return a+b

# print(add(7,8))

# added_number = add(7,8)

# # print(added_number)

# def check_num(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else: 
#         return "Zero"

# print(check_num(42))

# print (41 > 0)

# print(True and True)

# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen:
#         print("You can vote!")
#     else:
#         print("You cannot vote.")

# can_vote(19, True)

# def is_weekend(day):
#     if day=="Saturday" or day=="Sunday":
#         return "It is the weekend!"
#     else:
#         return "It is a weekday."

# print(is_weekend("Monday"))

# for i in range(10):
#     print(i)

# fruit_basket = ("lychee", "mango", "nectarines")

# for fruit in fruit_basket:
#     print(fruit)

# def countdown(start):
#     while start > 0:
#         print("T-",start)
#         start -= 1
#     print("Lift off!")

# countdown(10)

# Lecture 9/23

# list = [40,80,10,30,50,20]
# def minimum(list):
#     return min(list)

# print(min(list))

# def maximum(list):
#     return max(list)

# print(max(list))

# Determining whether a positive integer is a prime number with a function

# def isprime(num):
#     if num <= 0 or type(num) != int:
#         return "Try again, choose a new number."
#     else:
#         if num == 1:
#             return "Neither."
#         elif num == 2:
#             return "It's a prime number!"
#         else: 
#             if num % 2 == 0:
#                 return "It's a composite number!"
#             else:
#                 for i in range(1, num):
#                     if num % 1 == 0:
#                         return "It's a composite number!"
#                     else:
#                         return "It's a prime number!"

# print (isprime(34))

# Lecture 9/28

# Lists syntax

# numbers = [1, 2, 3, 4]

# print(numbers)

# fruits = ["apple", "cherries", "bananas"]

# print(fruits)

# mixed = ["Hello", 5, True, None]

# print(mixed)

# # Access items in a list

# print(numbers[0]) # First item

# print(fruits[-1]) # Last item

# fruits[0] = "grape" # Replaces item with that value with grape
# print(fruits)

# numbers.append(6) # Add 6 to the list

# print(numbers)

# print(mixed)

# print(mixed.insert(1, False))

# print(mixed)

# fruits.remove("bananas")

# print(fruits)

# print(numbers)
# numbers.pop

# print(numbers)

# for num in numbers:
#     print(num)

# fav_colors = ["yellow", "orange", "blue", "pink", "purple", "red"]
# print(fav_colors)
# print(fav_colors[1])
# print(fav_colors[-1])

# fav_colors.append("indigo")

# print(fav_colors)

# for color in fav_colors:
#     print(color)

# nums = [5, 4, 3, 2, 1]
# sub_nums = nums[1:4] # 1 is inclusive so it includes the second value (4) and 4 is exlusive so it does not include the 5th value (1)
# print(sub_nums)

# num_list = [10, 9, 8, 7, 6, 5, 4, 3, 2 ,1]
# print(num_list[::1])

# print(num_list[1:8:2])

# numb = [10, 20, 30, 40, 50, 60]
# print(numb[1:4])
# print(numb[:3])

# numbs = [20, 40, 60, 80, 100, 120]
# print(numbs[::2])

# [::-1] reverses list
# [-3:] gives the last 3

# Lecture 9/30
# bugs = {
#     "ants": ["black", "fire"],
#     "spiders": ["black widow", "tarantula"],
#     "flys": ["horse", "house"]
# }
# for values in bugs.values():
#     print(values)
# for keys in bugs.keys():
#     print(keys)
# for items in bugs.items():
#     print(items)

# list1 = list(range(0, 11)) # DO THIS TO FIX HW4
# print(list1)
# print(list1[0:5])
# print(list1[::2])
# print(list1[1::2])
# print(list1[-1])

# def get_first_5(list1):
#     return list1(list(range(0, 6)))
# print(get_first_5(list1))
# nested_list = {
#     "a": [2, 4, 6],
#     "b": [8, 10, 12],
#     "c": [14, 16, 18]
# }
# print(nested_list["c"][1])

stars_data = {
    "name": ["Sirius", "Vega", "Altair"],
    "magnitude": [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation": ["Canis Major", "Lyra", "Aquila"]
}

for name in stars_data["name"]:
    print(name)

def count_close_stars(data):
    count = 0
    for distance in data["distance_ly"]:
        if distance < 20:
            count += 1
        else:
            count += 0

print(count_close_stars())