#An element is called a leader if it is greater than or equal to every element to its right.
#The last element is always a leader because there are no elements to its right.

arr=list(map(int,input("enter your array:").split()))
leader = []
for i in range(len(arr)):
  is_leader=True
  #for every element, assume it's a leader
  for j in range(i+1,len(arr)):
   if arr[j] > arr[i]:
     #for every element, if there is any element to it's right is greater, then is_leader is set to false, means it's not a leader, otherwise it is added to leader[].
     is_leader = False
  #if is_leader = True then it appends the element.
  if is_leader:
    leader.append(arr[i])

print("leaders:", leader)