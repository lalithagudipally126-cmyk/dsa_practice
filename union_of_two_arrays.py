#Given two arrays, create a new array containing all the distinct elements from both arrays. Keep the order in which each element first appears: scan the first array, then the second.
arr1 = list(map(int, input("Enter your 1st array: ").split()))
arr2 = list(map(int, input("Enter your 2nd array: ").split()))
numbers=[]
for i in range(len(arr1)):
  if arr1[i] not in numbers:
    numbers.append(arr1[i])
for j in range(len(arr2)):
  if arr2[j] not in numbers:
    numbers.append(arr2[j])
print("array containing distinct elements from both arrays:",numbers)
#if we want to exclude elements that are in both arrays
num=[]
for k in arr1:
    if k not in arr2:
        num.append(k)
for l in arr2:
    if l not in arr1:
        num.append(l)
print("array without the elements which are in both;",num)