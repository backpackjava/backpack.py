import numpy as np
your_vector = np.array([1,2,3])
your_matrix = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]
                        ])

# Slicing
matrix_a = [1,2,3]
print(matrix_a[1:2]) # from item 1 to up to item 2 (not including item 2)
print(matrix_a[:2]) # everything up to item 2 (not including item 2)
print(matrix_a[1:]) # everything from item 1 to the end (including 1)
print(matrix_a[:]) # copy
print(matrix_a[::2]) # every second element
print(matrix_a[::-1]) # reverse
print(matrix_a[::-2]) # every second element in reverse
print(matrix_a[-1]) # last element

# uppercase, lowercase, replace
message = "hello"
print(message.upper())
print(message.lower())
print(message.replace("e", "u"))

# split and join
print(message.split("e")) # outputs a list of 2 items, not including splitted value
new_message = message.split("e")
print("e".join(new_message)) # outputs the splitted list and puts joined value between

# I, or identity matrix
matrix_I = np.identity(3)
print("I:\n", matrix_I)

# J (vector of ones), zeros, and empty
unit_vector = np.ones(3)
zero_vector = np.zeros(3)
empty_vector = np.empty
print("\nUnit Vector: ", unit_vector, "\nZero Vector: ", zero_vector, "\nEmpty Vector: ", empty_vector)

# Fill with same number or NaN
same_vector = np.full(6, 156)
nan_vector = np.full(6, np.nan)
print("\n156 Vector in 6 dimensions: ", same_vector)
print("NaN Vector: ", nan_vector)

# np.linspace(start, stop, number_of_elements)
# np.arange(start, stop, incrementby)
linspace_array = np.linspace(1,10,5)
arange_array = np.arange(1,13,2)
print("\nLinspace: ", linspace_array, "\nArange: ", arange_array)


print(your_matrix)
print("Row 1 of your_vector: ", len(your_matrix[0]))
print("Row 2 of your_vector: ", len(your_matrix[1]))
print("Row 3 of your_vector: ", len(your_matrix[2]))

# Shape and size of a matrix
print(your_matrix.shape)
print(your_matrix.size)

# Smallest and largest elements of an array
print(np.min(your_vector))
print(np.max(your_matrix))
# Location of them
print(np.argmin(your_vector))
print(np.argmax(your_matrix))
# Smallest and largest elements in a matrix's rows and columns
print(np.min(your_matrix, axis = 1)) # axis = 1 is rows
print(np.max(your_matrix, axis = 0)) # axis = 0 is columns
print(np.argmin(your_matrix, axis = 1)) # locations
print(np.argmax(your_matrix, axis = 0)) # locations

# Flatten, reshape, transpose
print(your_matrix.flatten())
print(np.transpose(your_matrix, (1,0))) # flips axes (switches rows and columns)

# Condition-based indices 
print(np.where(your_matrix > 30))
print(np.argwhere(your_matrix > -20))

# Sorting
print(np.sort(your_matrix))
print(np.sort(your_matrix, axis = 0)) # least to greatest in rows
print(np.sort(your_matrix, axis = 1)) # least to greatest in columns

# Coding Challenge from BWSIX:  Add 5 to every other element in my_matrix
my_matrix = [[[1]],[[2]],[[3]]] * np.ones((3,3,3))

flat_matrix = my_matrix.flatten()
count = 0
while count < len(flat_matrix):
    flat_matrix[count] = flat_matrix[count] + 5
    count += 2

print("")
# Coding Challenge from BWSIX: practice with flatten, reshape, and transpose

print(flat_matrix.reshape(3,3,3))

print(my_matrix.flatten())
print(my_matrix.reshape(3,9))
print("")
print(np.transpose(my_matrix, (2,1,0)))

