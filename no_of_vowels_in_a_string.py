text = input("Enter your string: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

# Count vowels
for i in text:
    if i in vowels:
        count += 1

print("Number of vowels:", count)

# Reverse the string
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
