# Dictionaries
# key in dictionaries can be strings or integers nothing else.

# storing marks of the student
# Satish is the key and 100 is the value
d = {'Satish': 100, 'Nitesh': 90, 'Kira': 95, 'Anil': 80}
print("Dictionary :", d)
l = d.keys()  # list created #d.keys() => Function of Dictionaries
b = d.values()  # list created #d.values() => Function of Dictionaries
print("keys :", l)
print("value :", b)

# We can't delete only key or only value if we want to delete we have to delete both.
del d['Satish']  # it will delete key satish and value of satish.
print("Dictionary :", d)

# Updation
d['Kira'] = 100
print("Dictionary :", d)
d['sks'] = 95
print("Dictionary :", d)

marks = d['Nitesh']
print("marks of Nitesh :", marks)

if ('sks' in d):
    print("Yes")
else:
    print("No")

# Length of dictionary
print("Length of dictionary d :", len(d))

# Difference between Dictionary and List is Dictionary have key value pairs but list doesn't
# & list is ordered whether dictionaries aren't(nothing like index is used in dictionary).

# for loop in dictionaries
for i in d:
    print(i, ":", d[i])

n = {1: [1, 2, 3], 2: [4, 5, 6]}  # Dictionary n, key = integer & values = list
print(n)
