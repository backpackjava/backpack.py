# Q.2 Please write a recursive function my_recursive_function that prints from 0 to 5:

def my_recursive_function(number = 0):
    """YOUR DOCSTRING HERE."""
    if number < 6:
        print(number)
        number += 1
        my_recursive_function(number + 1)
    pass

my_recursive_function()




def check_var_is_list(my_list):
    """Check if variable is a list."""
    if type(my_list) == list:
        return "my_list is a list"
    return "Input must be of type list" # THE FUNCTION ENDS after the return statement

print(check_var_is_list([1, 2, 3]))
print(check_var_is_list(2))
print(check_var_is_list("hello"))





import random as r
def greet_name(name):
    """this is a docstring, used to describe a function.
    This function greets the user, taking the name as a parameter and randomly choosing a greeting."""
    greeting_value = r.randrange(1,4)
    if greeting_value == 1:
        print(f"Hello, {name}!")
        return(f"Hello, {name}!")
    if greeting_value == 2:
        print(f"Greetings, {name}!")
        return(f"Greetings, {name}!")
    if greeting_value == 3:
        print(f"Nice to see you, {name}!")
        return(f"Nice to see you, {name}!") #need return value to store it in a variable

greeting = greet_name("Brian")
print(greeting) #for this to work, we needed a return value in the function 





Sally_choices = [3, 8, 12, 16, 18, 21, 22, 25, 27, 30]
Samantha_choices = [1, 4, 12, 17, 20, 21, 24, 25, 26, 28]
Susan_choices = [3, 5, 7, 9, 15, 18, 21, 22, 23, 25, 26, 27, 29]

def check_availabilities(person_one, person_two, person_three):
    good_choices = []
    largest = max(person_one, person_two, person_three, key=len)
    for date in largest:
        if date in person_one and date in person_two and date in person_three:
            good_choices.append(date)
    return(good_choices) #had to return it so we didnt have to take it out of the whole function

availabilities = check_availabilities(Sally_choices, Samantha_choices, Susan_choices)
print(availabilities)