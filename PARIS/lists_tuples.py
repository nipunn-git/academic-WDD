mylist=[1,2,3,4,31,345,7]
mylist.insert(4,13)
print("After inserting 13 at index 4: ", mylist)
mylist.sort()
print("After sorting in ascending order: ", mylist)
mylist.pop()
print("After deleting last element: ", mylist)
mylist.remove(31)
print("After removing 31: ", mylist)
mylist.reverse()
print("After reversing: ", mylist)
mylist.append(67)
print("After appending 67: ", mylist)
mylist.extend([20,30,40])
print("After extending the list: ", mylist)
count=0
temp_list = mylist.copy()
while temp_list:
    temp_list.pop()
count+=1
print(f"Number of elements in the list: {count}")

# Question 7 ) A Python program to accept elements in the form of a tuple
mylist=[]
n=int(input("Enter size of tuple: "))
for i in range(1,n+1):
    e=int(input(f"Enter element {i}: "))
    mylist.append(e)
mytuple=tuple(mylist)
sum=0
print(mytuple)
for item in mytuple:
    sum +=item
print(sum)
avg=float(sum/n)
print(avg)