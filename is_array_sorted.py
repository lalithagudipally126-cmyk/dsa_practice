#Given an array of integers, determine whether it is sorted in non-decreasing order.
#That means each element must be less than or equal to the next one.
arr = list(map(int, input("Enter your array now: ").split()))
is_sorted = True
for i in range(len(arr) - 1):
  if arr[i+1]-arr[i]<0:
    is_sorted = False
print("is array sorted:",is_sorted)