#  Question 1 —  Create a 1D array of numbers from 1 to 10.

'''import numpy as np

arr = np.array(np.arange(1,11))
print(arr)'''

# Q2. Create a 2D NumPy array with values from 1 to 9 arranged in a 3x3 matrix.

'''import numpy as np

arr = np.array([np.arange(1,10)])
new_arr = arr.reshape(3,3)
print(new_arr)'''

# Q3. Create a NumPy array of 5 zeros and another of 5 ones.  

'''import numpy as np

zero_array = np.zeros(5)
ones_array = np.ones(5)

print(zero_array)
print(ones_array)'''

# Q4. Create a NumPy array that contains only even numbers from 2 to 20 (inclusive).  
# Use any method you're comfortable with (np.arange, np.array, or slicing).

'''import numpy as np

arr = np.array(np.arange(2,21,2))
print(arr)'''

# Q5.  Given the array:
# arr = np.array([10, 20, 30, 40, 50])

# Write code to:
# 1. Print the first element  
# 2. Print the last element  
# 3. Print a slice containing elements [20, 30, 40]

'''import numpy as np
arr = np.array([10,20,30,40,50])

print(" first element:",arr[0])
print(" last element:",arr[4])
print("elements [20, 30, 40]:",arr[1:4])'''

# Q6. Given arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]),  
# print:
# 1. Element at second row, third column  
# 2. Entire second row  
# 3. All elements of third column

'''import numpy as np

arr = np.array([[10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]])

print("1. Element at second row, third column:", arr[1,2])
print("2. Entire second row:", arr[1])
print("3. All elements of third column:", arr[:, 2])'''

# Q8. Given an array arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]),  
# write code to extract a subarray containing every second element starting from index 1 to 7.
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(arr[1:8:2])'''

# Q8. Replace all even numbers in the array
#  arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) with -1.

'''import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9])
arr[arr % 2 == 0] = -1
        
print(arr)'''

# Q10. Create a 1D array of numbers from 1 to 12, then reshape it into a 3x4 matrix.
# Try writing the code to:
# 1. Create the array.
# 2. Reshape it.
# 3. Print the reshaped matrix.

'''import numpy as np

matrix = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(matrix)
new_matrix = matrix.reshape(3,4)
print(new_matrix)'''

# 1. Importing NumPy  
# ✅ Q1. Import NumPy and print its version.

'''import numpy as np
print(np.__version__)'''


# Q2. Create a 1D NumPy array containing numbers from 1 to 5,  
# and a 2D NumPy array with 2 rows and 3 columns filled with any numbers.  
# Then print both.

'''import numpy as np

arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_1d)
print(arr_2d)'''


# 3. Using arange(), linspace(), zeros(), ones()  
# ✅ Q3. Create:  
# - an array from 0 to 20 with step 5 using arange()  
# - 5 values between 0 and 1 using linspace()  
# - an array of five zeros  
# - a 2×2 array of ones

'''import numpy as np

arr = np.arange(0,21)
linspace = np.linspace(0,1,5)
zero_array = np.zeros(5)
ones_array = np.ones((2,3))

print(arr)
print(linspace)
print(zero_array)
print(ones_array)'''

# Q: Create a NumPy array with elements [1, 2, 3, 4] of type float64. 
# Then print the array and its data type (dtype).  

'''import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)
new_arr = arr.astype(float)
print(new_arr.dtype)'''

# Q5. Convert the following list of lists into a 2D 
# NumPy array and print its shape.
# data = [[1, 2, 3], [4, 5, 6]]

import numpy as np

data = [[1, 2, 3], [4, 5, 6]]
arr = np.array(data)

print(arr.ndim)
print(arr.shape)





