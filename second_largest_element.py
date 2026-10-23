arr = list(map(int, input("Enter your array: ").split()))
largest_number = arr[0]
second_largest_number=0
for i in range(1,len(arr)):
  if arr[i] > largest_number:
    second_largest_number = largest_number
    largest_number = arr[i]
  elif arr[i] < largest_number and arr[i] > second_largest_number:
    second_largest_number = arr[i]
print("largest number:",largest_number)
print("second largest number:", second_largest_number)