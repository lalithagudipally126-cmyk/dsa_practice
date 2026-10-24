#all the zeros should be at the end
arr = list(map(int, input("Enter your array: ").split()))
print("array before moving all the zero's to the end:",arr)
non_zeros = []
zeros = []
for i in arr:
  if i==0:
    zeros.append(i)
  else:
    non_zeros.append(i)
arr1 = non_zeros + zeros
print("array after moving all the zero's to the end:",arr1)
    