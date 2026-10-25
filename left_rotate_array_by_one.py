#Given an array, move the first element to the end and shift every other element one position to the left.
#Example 1
#Input:  [1, 2, 3, 4, 5]
#Output: [2, 3, 4, 5, 1]
arr = list(map(int, input("Enter your array now: ").split()))
x = arr.pop(0)
arr.append(x)
print("after left shift:",arr)
