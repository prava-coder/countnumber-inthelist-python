#python program to count the occurence of a particular element in the list
import time
list1=[1,1,1,2,1]
print(list1)
print("the length of the list is:",len(list1))
count=0
user_input=int(input("enter any one number in the given list:"))
print("counting the number how many times appeared in the list...")
time.sleep(3)
for num in list1:
    if num==user_input:
        count+=1
print(count)
