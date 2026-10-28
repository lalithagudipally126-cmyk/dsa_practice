#Given an array and an integer k, rotate the array to the left by k positions.
arr=list(map(int,input("enter your array:").split()))
j=int(input("enter the element till which you want the array to rotate left:"))
result=[]
for k in range(len(arr)):
  if arr[k]==j:
    position=k
for i in range(position,len(arr)):
  result.append(arr[i])
for l in range(len(arr)-position-1):
  result.append(arr[l])
print("after left rotation:",result)