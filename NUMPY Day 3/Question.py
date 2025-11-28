'''
🔹 Day 3: Mathematical Operations & Statistics
Topics:
- Element-wise operations
- Aggregations: sum, mean, std, min, max, median, var
- Broadcasting
- Boolean indexing

Practice (12 questions):
1. Extract all elements greater than 30 from arr = np.array([10, 25, 30, 45, 50]).
2. From arr = np.array([5, 15, 25, 35, 45]), extract all even numbers.
3. Create a new array of only elements divisible by 5 from arr = np.array([7, 10, 12, 15, 20]).
4. Find the min and max of arr = np.array([6, 1, 8, 3]).
5. Find the sum of each row in  

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

06. Find the mean of each column in the same array.  
07. Find sum, mean and standard deviation of an array.
08. Replace all values less than 5 with 0.
09. Add two arrays of the same shape.
10. Use broadcasting to add a 1D array to each row of 2D array.
11. Find max element and its index.
12. Count how many values are even in a given array.
'''

# ====== Let's start Day 3 of practicing question ====== #

# 1. Extract all elements greater than 30 from
# arr = np.array([10, 25, 30, 45, 50]).

'''import numpy as np
arr = np.array([10, 25, 30, 45, 50])

new_arr = arr[arr>30]

print(new_arr)'''

# 2. From arr = np.array([5, 15, 25, 35, 45]), extract all even numbers.

'''import numpy as np

arr = np.array([5,15,25,35,45])
new_arr = arr[arr%2 == 0]

print(new_arr)'''

# 3. Create a new array of only elements divisible 
# by 5 from arr = np.array([7, 10, 12, 15, 20]).

'''import numpy as np

arr = np.array([7, 10, 12, 15, 20])

new_arr = arr[arr %5 == 0]
print(new_arr)'''

# 4. Find the min and max of arr = np.array([6, 1, 8, 3]).

'''import numpy as np

arr = np.array([6,1,8,3])
print("Max elements of arr: ", np.max(arr), ", Min elements of arr: ",np.min(arr)) '''

# 5. Find the sum of each row in  
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

'''import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Sum of 1st row = ", np.sum(arr[0]),", Sum of 2nd row = ", np.sum(arr[1]))'''

# 06. Find the mean of each column in the same array.  

'''import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"mean of 1st column: {np.mean(arr[:,0])}, mean of 2nd column: {np.mean(arr[:,1])}, mean of 3rd column: {np.mean(arr[:,2])}")'''

# 07. Find sum, mean and standard deviation of an array.
'''
import numpy as np

arr = np.array([10,20,30,40,50,60])

print(f"Sum of all Elements: {np.sum(arr)}\nMean of all Elements: {np.mean(arr)}\nStandard Deviation of all Elements: {np.std(arr)}")'''

# 08. Replace all values less than 5 with 0.

'''import numpy as np

arr = np.array([[1,2,3],[4,5,6],[6,5,8,]])
arr[arr<5] = 0
print(arr)'''

# 09. Add two arrays of the same shape.
'''import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(arr1 + arr2)'''


# 10. Use broadcasting to add a 1D array to each row of 2D array.
'''import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 10, 10])

print(arr1 + arr2)'''


# 11. Find max element and its index.
'''
import numpy as np

arr = np.array([1,55,68,6,3,58,69,45,12])

print(f"Maximum element: {np.max(arr)}, Index of Max element: {np.argmax(arr)}")'''


# 12. Count how many values are even in a given array.

'''import numpy as np

arr = np.array([1,55,68,6,3,58,69,45,12])
count = np.sum(arr % 3 == 0)

print(count)'''


