a = [6, 2, 3, 9, 1, 6, 4, 5]
print(len(a))
print(max(a))
print(min(a))
s = "iamsks"
print(list(s))
print(sum(a))
for element in a:
    print(element * 2, end=" ")

a = [6, 2, 3, 9, 1, 6, 4, 5]
fruits = ['Banana', 'Apple', 'Kiwi', 'Kiwi']
a.pop(0)
print('\n', a)
a.clear()
print(a)
fruits.reverse()
print(fruits)
print(fruits.index('Apple'))
print(fruits.count('Kiwi'))
a.sort()
print(a)
fruits.sort()
print(fruits)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [x for x in range(24) if x % 2 == 1]  # list created
print(a)
b = [3**i for i in range(10)]
print(b)

name = 'iamsks'
print(name)
name = 224
print(name)
fruits = ["Apple", 'Guava', 'Papaya']
print(fruits[-1])
fruits[1] = 'Mango'
print(fruits)
del fruits[0]
print(fruits)
# del fruits  # whole list will be deleted

# List Methods
print('\nList Methods')
l = [1, 2, 3, 4, 6]
print(l)
l.append(4)  # last position pe 4 aajaayega in the list
print(l)
l.insert(0, 5)  # 5 insert ho jaayega in the list at index = 0
print(l)
l.sort()
print(l)
l.pop(0)
print(l)
l.reverse()
print(l)
print(l.index(3))  # index of 3 present in the list
print(l.count(4))  # count no. of times 4 is in the list
l.insert(3, 'i am sks')
print(l)
l.clear()
print(l)

# List Functions
print('\nList Functions')
ls = [12, 24, 36, 2001, 48, 60]
print(len(ls))
print(max(ls))
print(min(ls))
print(sum(ls))
str = 'iamsks'
print(list(str))  # string into list

# for loops with Lists
print('\nfor loops with Lists')
l1 = [1, 6, 5, 3, 0, 2, 5, 4, 7]
for i in l1:
    print(i*2, end=" ")


# new codes
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
