#Given a array, create a new array containing only the distinct elements, while keeping their original order.
arr = list(map(int, input("Enter your array now: ").split()))
numbers = []
for i in range(len(arr)):
  if arr[i] not in numbers:
    numbers.append(arr[i])
print(numbers)