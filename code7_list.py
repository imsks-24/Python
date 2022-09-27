# Lists
l1 = []  # empty list
print("Empty List l :", l1)
l = [1, 5, 7, 10, 24]
print("List l1 :", l)
print("l[0] :", l[0])
# List Slicing
print("l[2:4] :", l[2:4])  # from index = 2 to index = 3 print ho jaayega
l.append(24)  # this will add/insert 24 in the list at last position
print("l :", l)
b = [20, 100]
l.extend(b)  # b list will be added in list l
print("l :", l)

# insert the element in the list at any position you want
# list l mai 2nd index pe 99 daal do baaki elements shift ho jaayenge
l.insert(2, 99)
print("l :", l)

# Sort the list
l.sort()
print("l :", l)

# delete an element from the list
l.pop(2)  # it will delete element present at index = 2
print("l :", l)

# count an element from the list
cnt = l.count(24)  # it will count the no. of 24 in the list
print("cnt :", cnt)

# List Length
s = len(l)
print("Length of l :", s)

# Sum of all the elements in the list
sum = sum(l)
print("sum of all the elements in the list l:", sum)

x = l*3  # list l ko 3 baar ek ke peeche lga dega
print("x :", x)

# for loop in list
for i in range(len(l)):
    print("l[", i, "] :", l[i])

t = []  # empty list
n = 4  # size of the list
for i in range(n):
    print("list t[", i, "] :")
    num = int(input())
    t.append(num)

print("List t:", t)
