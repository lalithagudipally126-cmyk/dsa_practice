#Find the intersection of two arrays
#Given two arrays, find the elements that appear in both arrays, without repeating any element in the result.
arr1=list(map(int,input("enter your first array:").split()))
arr2=list(map(int,input("enter your second array:").split()))
result = []
for i in range(len(arr1)):
  if arr1[i] in arr2 and arr1[i] not in result:
    result.append(arr1[i])
print("elements that appear in both arrays:",result)