arr = list(map(int, input("Enter your array: ").split()))
reversed_array1 = []
reversed_array2 = []
reversed_array3 = []
print("array:",arr)
print("reversed_array directly:", arr[::-1])
reversed_array1.extend(reversed(arr))
#reversed() reverses the order of the elements.
#extend() takes those elements and adds them one by one.
print("reversed_array using .extend(reversed()):",reversed_array1)
for x in reversed(arr):
    reversed_array2.append(x)
print("reversed_array using for loop and reversed() and append():",reversed_array2)
#range(start,stop,step)
#len(arr)-1 means length -1 which is how many indexes an array has so it's like starting for the last index
# Stop value is -1, but the stop value is excluded.
# So Python stops before reaching -1, which means index 0 is included.
#for step we use -1 cause we only want it to go one element at a time, Move backward one position each iteration.
for i in range(len(arr)-1,-1,-1):
  print(arr[i])
  reversed_array3.append(arr[i])
print(reversed_array3)