#Given an array of integers, move all negative numbers to the beginning and all non-negative numbers to the end.
#For this problem, preserve the original order of the negative numbers and the non-negative numbers
#Your rules
#- Use a loop.
#- Create a new list.
#- Don't use sort() or sorted().
#- Remember that zero is not negative.

arr = list(map(int, input("Enter your array now: ").split()))
neg_num=[]
pos_num=[]
arr1=[]
for i in range(len(arr)):
  if arr[i] < 0:
    neg_num.append(arr[i])
  else:
    pos_num.append(arr[i])
for i in neg_num:
  arr1.append(i)
for i in pos_num:
  arr1.append(i)
print("array after all the negative numbers are moved to the front:",arr1)