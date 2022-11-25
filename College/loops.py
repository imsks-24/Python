# while loop
n = 5
while n >= 0:
    print(n)
    n -= 1

# for loop
for x in range(10):
    print(2*x, end=", ")

a = ['iamsks', 'nks', 'major']
print('\n')
for name in a:
    print(name*2)

# break
for i in range(10):
    if i > 6:
        print(i)
        break

# continue
for i in range(10):
    if i == 8:
        continue
    print(i, end=" ")


# start from 0.
for i in range(4):  # i will start from 0 . and it will run from 0-3(4 times)now it will increment by i = i+1
    print("i : ", i)
# start from 2.
for j in range(2, 4):  # j will start from 2 . and it will run from 2 to 3 (2 times)now it will increment by j = j+1
    print("j : ", j)
# increment by 2.
for k in range(2, 4, 2):  # j will start from 2 . and it will run from 2 to 3 (1 times).now it will increment by k = k+2
    print("k : ", k)
