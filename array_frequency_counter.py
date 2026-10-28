#Given an array of integers, count how many times each distinct element appears.
arr=list(map(int,input("enter your array:").split()))
numbers=[]
count=[]
for i in range(len(arr)):
  if arr[i] not in numbers:
    numbers.append(arr[i])
for l in range(len(numbers)):
  count.append(0)
for j in range(len(arr)):
  for k in range(len(numbers)):
    if arr[j] == numbers[k]:
      count[k] +=1
for m in range(len(numbers)):
  print(f"in the array {numbers[m]} repeats {count[m]} times")