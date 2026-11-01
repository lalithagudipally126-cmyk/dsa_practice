# Find the equilibrium index
#An index is an equilibrium index if the sum of all elements to its left equals the sum of all elements to its right. The element at that index is excluded from both sums.
#task: Write a Python program that finds the first equilibrium index. If none exists, print -1.
arr=list(map(int, input("enter your array:").split()))
found = False
for i in range(len(arr)):
  right_sum=0
  left_sum=0
  for j in range(i+1,len(arr)):
    right_sum += arr[j]
  for k in range(0,i):
    left_sum +=arr[k]
  if left_sum == right_sum:
    print(f"{i} is the equlibrium index.")
    found = True
if found == False:
  print("-1")