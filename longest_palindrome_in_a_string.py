string = input("enter your string:")
n=len(string)
x=""
for i in range(0,n):
  for j in range(i+1,n+1):
    substring = string[i:j]
    reverse_substring=substring[::-1]
    if substring == reverse_substring:
      if len(substring) > len(x):
        x = substring

print("substring", x, "len of substring:", len(x))