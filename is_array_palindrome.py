#is the array a palindrome?
arr = list(map(int,input("enter your array:").split()))
reversed=[]
if arr == arr[::-1]:
  print("palindrome")
else:
  print("not palindrome")
#len(arr -1) means starting from the last index
#next, stop, which is -1, -1 is used so it reaches till the first index, which is 0
#next, step -1, meaning it skips to next element(go back one step)
for i in range(len(arr)-1,-1,-1):
  reversed.append(arr[i])
if arr == reversed:
  print("palindrome")
else:
  print("not palindrome")
    