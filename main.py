import random as random

# shorthand for appending
list = [i for i in range(10)]
print(list)
# prints out [0,1,2,3,4,5,6,7,8,9]

# counter = 0
# for i in range(5):
#     decider = random.randint(1,2)
#     if decider == 1:
#         counter += 1
#         # increment
#     else:
#         counter -= 1
#         # decrement
#     print (counter)

# # item is a loop variable and tuple: 
# # in list item ("Hello", "Greeting"), item[0] is "Hello" and item[1] is "Greeting"
# sayings = [("Hello", "Greeting"), ("What's Up", "Greeting"), ("See you", "Goodbye")]
# for item in sayings:
#     print(f"{item[0]} is a {item[1]}")

# random_int = random.randint(0,10)
# print(random_int)
# if random_int > 5:
#     print(f"{random_int} is greater than 5")
# elif random_int == 0:
#     print(f"{random_int} is equal to 0")
# elif random_int is 5:
#     print(random_int, "is 5.")
# else: 
#     print(f"{random_int} is less than 5")


# random_integers = []
# for i in range(5):
#     random_integers.append(random.randint(0,10))
# print(random_integers)
# if 6 in random_integers:
#     print("6")
# if 7 in random_integers:
#     print("7")
# if 6 in random_integers and 7 in random_integers:
#     print("6 7!")