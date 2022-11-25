password = "abcdABA$"
print(password.isalpha())

s = "ABCDE$%"
print('s.isalpha', s.isalpha())
print('s.isdigit', s.isdigit())
print('s.islower', s.islower())
print('s.isupper', s.isupper())

print('s.lower', s.lower())
print('s.upper', s.upper())

x = '   abc def ghi   a'
print(x.lstrip())
print(x.rstrip())

a = "abc"
for my_char in a:
    print(my_char * 2)

b = 'def'
c = a + b
print(c)
c = a * 3
print(c)

fruit = "Apple"
print(fruit[4])
print(fruit[-2])
my_char = fruit[2]
print(my_char)

name = "Satish Kumar Shah"
paragraph = '''This is a multiline
String paragraph.
This is for testing'''
print(name)
print(paragraph)

# string slicing
str = 'iamsks'
print(str[:1], "", str[1:3], "", str[3:])
str1 = 'Satish Kumar Shah'
print(str1[1:18:2], "", str1[::2], "", str1[1::3])
str2 = 'abcde'
print(str2[-1:-4:-1], "", str2[::-1], "", str2[-1:-4:-2])
print(str2[-1:1:-2])

# string functions
str2 = "imSatishKumarShah imSatishKumarShah imSatishKumarShah"
str3 = "SatishKumarShah"
print("str3 comes in str2 : ", str2.count(str3), " times")
if (str3 in str2):
    print('yes')
else:
    print('no')

str4 = "i am satish"
sks = str4.replace(" ", "@")  # space ko @ se replace kardo in string str4
print("str4 after replacing : ", sks)
for i in str4:
    print("str4 : ", str4)

if (str2.find(str3) >= 0):  # or if (str3 in str2):
    print("str3 is present in str2")
else:
    print("str3 is absent in str2")


str1 = "imSatishKumarShah"
# find function() : if str3 is not in str4 then it will return -1.
print("str3 present in str2 at index : ", str2.find(str3))
