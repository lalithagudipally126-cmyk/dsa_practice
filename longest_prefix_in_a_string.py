x=int(input("Enter the no. of strings:"))
n=0
words=[]
while n<x:
  string = input(f"Enter your string {n+1}:")
  words.append(string)
  n+=1
print("Given list of strings:",words)
prefix =""
i=0
j=0
for j in range(len(words[i])):
#if words[0][j] != words[i][j]:break checks whether two characters are different(like first character of first word with first character of second word and so on third word, etc also then goes to second character comparision next cause of loops).
#- If they're different, break stops the inner loop.
#- If they're the same, nothing happens, and the inner loop continues checking the other words.
  for i in range(1, len(words)):
#in this if, First condition: Does this word have a character at this position?
#Second condition: If it does, does that character match?
    if j >= len(words[i]) or words[0][j] != words[i][j]:
      break
#the else block belongs to for i in range(1, len(words)):
#Python has a special feature called for...else.
#so the else blocks runs till it encounters break through if. 
#so basically both if and else run until it breaks(there is a mismatch)
  else:
    prefix += words[0][j]
    continue
#this break belongs to for j in range(len(words[i])):
#this causes the outer loop to break when the inner loop breaks.
  break

print("longest prefix:",prefix)
