import numpy as np

# I, or identity matrix
matrix_I = np.identity(3)
print("I:\n", matrix_I)

# J (matrix of ones), zeros, and empty
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

your_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(your_matrix)
print("Row 1 of your_vector: ", len(your_matrix[0]))
print("Row 2 of your_vector: ", len(your_matrix[1]))
print("Row 3 of your_vector: ", len(your_matrix[2]))

# Shape and size of a matrix
print(your_matrix.shape)
print(your_matrix.size)

