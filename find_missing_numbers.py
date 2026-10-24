#Given an array of distinct numbers from 1 to n, with one number missing.
#Find and print the missing number.
print("✨finding the missing number!!")
a = int(input("enter the positive integer till which you are entering from 1 into the array to find the missing numbers:"))
arr = list(map(int, input("Enter your array now: ").split()))
numbers = []
missing_numbers = []
for i in range(1,a+1):
  numbers.append(i)
print("numbers:",numbers)
for num in numbers:
  if num not in arr:
      missing_numbers.append(num)
print("missing numbers:",missing_numbers)
