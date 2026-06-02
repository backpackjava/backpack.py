# Breaking an infinite loop

import time as t
number = 0
start = t.time()

print("I am counting...")

while True:
    print(number)
    number += 1
    if t.time() > start + 0.1:
        break
# use time to BREAK loop after specific time interval

# break: stop loop
# continue: ignore everything under and go to next loop
# pass: go on (null)

# Q.1 We want to print all the ingredients in the list, 
# but we are out of milk. If we get to "milk" element in
# the list, print "We are out of milk!" and stop printing ingredients.
ingredients = ["eggs", "flour", "vanilla extract", "sugar", "milk", "vegetable oil", "water"]

for ingredient in ingredients:
    if ingredient == "milk":
        print("We are out of milk!")
        break
    print(ingredient)

# Q.2 Loop through the grades and print "pass" or "fail". If a grade is incomplete, print nothing.
grades = ["B", "incomplete", "A", "F", "C", "incomplete", "A", "F"]

for grade in grades:
    if grade == "F":
        print("Fail")
        continue
    if grade == "incomplete":
        continue
    print("Pass")

# Q.3 Given a number, print a countdown to zero from that number, but do NOT print the number 7.
# Example: given number = 10, your code should print: 10 9 8 6 5 4 3 2 1.
number = 10

while not number == 0:
    if number == 7:
        number -= 1
        continue
    print(number)
    number -=1

import random as random

# shorthand for appending
list = [i for i in range(10)]
print(list)
# prints out [0,1,2,3,4,5,6,7,8,9]

counter = 0
for i in range(5):
    decider = random.randint(1,2)
    if decider == 1:
        counter += 1
        # increment
    else:
        counter -= 1
        # decrement
    print (counter)

# item is a loop variable and tuple: 
# in list item ("Hello", "Greeting"), item[0] is "Hello" and item[1] is "Greeting"
sayings = [("Hello", "Greeting"), ("What's Up", "Greeting"), ("See you", "Goodbye")]
for item in sayings:
    print(f"{item[0]} is a {item[1]}")

random_int = random.randint(0,10)
print(random_int)
if random_int > 5:
    print(f"{random_int} is greater than 5")
elif random_int == 0:
    print(f"{random_int} is equal to 0")
elif random_int is 5:
    print(random_int, "is 5.")
else: 
    print(f"{random_int} is less than 5")


random_integers = []
for i in range(5):
    random_integers.append(random.randint(0,10))
print(random_integers)
if 6 in random_integers:
    print("6")
if 7 in random_integers:
    print("7")
if 6 in random_integers and 7 in random_integers:
    print("6 7!")