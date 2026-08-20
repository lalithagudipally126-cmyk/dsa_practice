nums = [3, 8, 5, 10, 7, 6]

list1 = []
count = 0

for i in nums:
    if i % 2 == 0:
        list1.append(i)
        count += 1

print("list:", list1)
print("even number count:", count)