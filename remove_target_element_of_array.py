#Write a Python program that:
#1. Takes an array as input.
#2. Takes a target number as input.
#3. Removes every occurrence of that number.
#4. Prints the resulting array
arr = list(map(float,input("enter your array:").split()))
num = float(input("enter the target number:"))
result =[]
for i in range(len(arr)):
  if arr[i] != num:
    result.append(arr[i])
print("after the target element is removed:",result)