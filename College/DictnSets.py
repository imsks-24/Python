# Sets : In sets duplicate elements are not allowed.
a = {1, 2, 4, 6, 4, 6, 1}  # sets
print('sets\n', a)
# print(a[0]) # indexing is not supported in sets
for i in a:
    print(i*2, end=" ")

# Dictionary
print('\nDictionary')
marks = {'Satish': 95, 'Nitesh': 95, 'sks': 84,
         'nks': 79, 24: 2001}  # key : value
print(marks)
print(marks['Satish'])
print(marks[24])
marks['Major'] = 90  # updating dictionary
marks[9] = 68  # updating dictionary
marks['nks'] = 81  # marks updated of nks
print(marks)
k = marks.keys()  # keys printing
print("keys : ", k)
v = marks.values()  # values printing
print('values : ', v)

#Iteration in dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print('Squares : ')
for i in squares:
    print(i, ':', squares[i])  # key : value

n = {1: [1, 2, 3], 2: [4, 5, 6]}  # Dictionary n, key = integer & values = list
print(n)

if ('sks' in marks):
    print('sks is present')
else:
    print('sks is absent')

print('Length of marks : ', len(marks))

# We can't delete only key or only value if we want to delete we have to delete both.
del marks['Satish']  # it will delete key satish and value of satish.
print("Dictionary :", marks)
