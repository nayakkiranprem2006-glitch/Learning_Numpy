'''🔹 Day 2: Array Indexing, Slicing & Reshaping
Topics:
- Indexing and slicing
- Reshape, flatten
- Array attributes (shape, ndim, etc.)
- Copy vs view

Practice (10 questions):
1. Access the 3rd element from a 1D array.
2. Slice the first 2 rows and 2 columns of a 3x3 array.
3. Reshape a 1D array of 12 elements to 3x4.
4. Flatten a 2D array.
5. Reverse an array.
6. Access last row of a 2D array.
7. Replace the element 5 with 50 in a 2D NumPy array.  
8. Demonstrate shallow vs deep copy.
9. Modify a slice of array and observe effect on original array.
10. Replace the middle element of a 1D array with 0.'''

# ====== Let's start practicing question ====== #

# Question 1. Access the 3rd element from a 1D array.

'''import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[2])'''

# 2. Slice the first 2 rows and 2 columns of a 3x3 array.

'''import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[:2, :2])'''


# 3. Reshape a 1D array of 12 elements to 3x4.

'''import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

new_arr = arr.reshape(3,4)
print(new_arr)'''

# 4. Flatten a 2D array into 1D array.

'''import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

new_arr = arr.flatten()

print(new_arr)'''

# 5. Reverse an array.
'''import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
new_arr = arr.T

print(new_arr)'''

# Q6. Access the last row of a 2D NumPy array.  

'''import numpy as np

arr= np.array([[1,2,3],[4,5,6]])
print(arr[1])'''

# Q7. Replace the element 5 with 50 in a 2D NumPy array.  

'''import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
arr[1,1]= 50
print(arr)'''

# 8. Demonstrate shallow vs deep copy.

'''import numpy as np
arr = np.array([1,2,3])

# shallow copy
shallow_arr = arr
shallow_arr[1] = 98
print("Original arr", arr)

# deep copy

deep = arr.copy()
deep[1] = 88
print("original arr", arr)
print("deep copy :", deep)'''

# Q10.  Add the 1D array [1, 2, 3] to each row of the 2D array:  
# [[10, 20, 30], [40, 50, 60], [70, 80, 90]].

'''import numpy as np
arr = np.array( [[10, 20, 30], [40, 50, 60], [70, 80, 90]])
new_arr = np.array([1,2,3])
array = arr + new_arr
print(array)'''

# Q11. Find unique elements in a NumPy array.

'''import numpy as np

arr = np.array([5,4,4,5,1,4,56,35,2,5,8])
unique = np.unique(arr)
print(unique)'''