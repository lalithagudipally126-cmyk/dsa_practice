# Find the largest number

nums = [4, 1, 9, 2, 7]

temp = nums[0]

for i in range(1, len(nums)):
    if nums[i] > temp:
        temp = nums[i]

print(temp)