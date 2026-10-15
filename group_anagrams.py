print("Group Anagrams")
y=int(input("Enter the no. of strings:"))
n=0
words=[]
while n<y:
  string = input(f"Enter your string {n+1}:")
  words.append(string)
  n+=1
print("Given list of strings:",words)
sorted_words=[]
#"".join() is used to combine a list of characters into a string
for i in words:
  x = sorted(i)
  z = "".join(x)
  sorted_words.append(z)
groups={}
for i in range(len(words)):
  key = sorted_words[i]
  if key in groups:
    groups[key].append(words[i])
  else:
    groups[key] = [words[i]]
print("Group Anagrams:",groups)