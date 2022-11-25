# 2D List : Lists within a List.
l = [[2, 3, 5], [1, 8, 9], [6, 7, 10], [12, 24.36]]
for element in l:
    print(element)

l1 = []
a = list(map(int, input("Enter the list a : ").split()))
b = list(map(int, input("Enter the list b : ").split()))
c = list(map(int, input("Enter the list c : ").split()))
l1.append(a)
l1.append(b)
l1.append(c)
print(l1)

# Recursion
# 1. Factorial of a Number


def fact(a):
    # Base Case
    if (a == 1):
        return 1
    else:
        return a*fact(a-1)


x = int(input("Enter a No. : "))
factorial = fact(x)
print('Factorial is :', factorial)
