# Find the second smallest distinct element
arr = list(map(int, input("enter your array: ").split()))
if len(arr) == 0:
    print("List is empty. No smallest or second smallest element.")
else:
    num1 = arr[0]
    num2 = None
    for i in range(len(arr)):
        if arr[i] < num1:
            num2 = num1
            num1 = arr[i]
        elif arr[i] > num1 and (num2 is None or arr[i] < num2):
            num2 = arr[i]
    print("smallest number:", num1)
    if num2 is None:
        print("second smallest number: doesn't exist")
    else:
        print("second smallest number:", num2)
#so if the list is empty, if len(arr) ==0, checks the length prints that there are no elements
#if there is one element, for example 1
#it will be assigned t num1, smallest element
#if arr[i] < num1 first check if the current element is smaller than num1, since there is only one element, it will be the current element and it will be equal , not smaller, so num2 stays none, it checks the elif, condition, elif condition first checks if it is larger than num1, it is not, it would be equal, and num2 is still none, which is checked in the second part, but since it is and and one condition is failed, the whole condition is skipped, so num2 still stays none. then we check if num2 is none, if it is we print that second smallest doesn't exist
#suppose we have an array 3 1 2
#first we check if the list/array is empty, it is not, so we proceed
#so first element is assigned to num1
#and then we go through one by one element
# so our current element is 3 and num1 is also 3
#so we check the first condition is arr[i] <num1? (3<3) no so we go to elif is (3>3)? no, 3 is not greater than 3, we go to next element 1, is one smaller than 3? yes, so num2 becomes 3 from none, and num1 becomes 1 from 3 , no need to go to elif cause 1 is true for this condition. next element 2 is 2 smaller than 1? no so next condition elif, is 2 greater than num1(1)? yes, 2 is greater than 1. then the other part checking, is num2 none? no, or is num2 greater than current element? (3 >2)? yes, so update num2 to 2. list/array is complete so the loop stops, and smallest element is printed and then for second smallest element , we have a condition to check is num2 none or not, num2 is not none, so it will printed as second smallest element.
#this also works for negative numbers in a similar manner.