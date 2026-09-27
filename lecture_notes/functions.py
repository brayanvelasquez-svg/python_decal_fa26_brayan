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

def isprime(num):
    if num <= 0 or type(num) != int:
        return "Try again, choose a new number."
    else:
        if num == 1:
            return "Neither."
        elif num == 2:
            return "It's a prime number!"
        else: 
            if num % 2 == 0:
                return "It's a composite number!"
            else:
                for i in range(1, num):
                    if num % 1 == 0:
                        return "It's a composite number!"
                    else:
                        return "It's a prime number!"

print (isprime(34))