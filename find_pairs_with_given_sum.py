#given an array and target number
#find the pair in the array that add up to the target
arr=list(map(int,input("enter your array:").split()))
target = int(input("enter your target number:"))
result=[]
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[i]+arr[j] == target:
      result.append((arr[i],arr[j]))
if len(result) != 0:
  print("pairs of elements that add up to the target:",result)
else:
  print("there are no pair of elements that add up to the target.")