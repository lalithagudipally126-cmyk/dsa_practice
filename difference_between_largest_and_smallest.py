#given an array, find the difference between the largest and the smallest element
arr=list(map(int,input("enter your array:").split()))
smallest=arr[0]
largest=arr[0]
for i in range(len(arr)):
  if arr[i] > largest:
    largest=arr[i]
for j in range(len(arr)):
  if arr[j] < smallest:
    smallest=arr[j]
print(f"difference between the largest element({largest})and the smallest element({smallest}) of an array:",largest-smallest)