str1 = "imSatishKumarShah"
print("str1[2] : ", str1[2])
print("Length of the string : ", len(str1))  # string length

# String slicing
s = str1[1:6]  # 1 to 5 index tak ki string ko fetch karlega
print("string str after slicing : ", s)
print("str1[:6] : ", str1[:6])  # from index 0 to index 5 sab print ho jaayega
# from index 3 to end of the string sab print ho jaayega
print("str1[3:] : ", str1[3:])
# index = -1 str[-1] = h(last element), index = -3 str[-3] = i
# index -3 aur -2 tak sab print ho jaayega
print("str1[-3:-1] : ", str1[-3:-1])
# from index = 6 se 10 tak 1 element skip karke print ho rha hai(from index = 6 every 2nd element is printing)
print("str1[6:11:1] : ", str1[6:11:2])
print("str1[::4] : ", str1[::4])  # from index 0, every 4th element is printed
# from index -2, every -2 element is printed
print("str1[::-2] : ", str1[::-2])
# from index = 3 saari string print ho jaayegi
print("str1[3::] : ", str1[3::])
# from index = -2 to index = -1 print ho jaayega
print("str1[-2::] : ", str1[-2::])

# counting the letters/characters in a string
print("S letter in the string str1 is : ",
      str1.count("S"), " times")  # case sensitive

# We can check to see where the first “h” occurs in the string str1
print("letter h occurs first at position : ", str1.find("h"))

str2 = "imSatishKumarShah imSatishKumarShah imSatishKumarShah"
str3 = "SatishKumarShah"
print("str3 comes in str2 : ", str2.count(str3), " times")
# find function() : if str3 is not in str4 then it will return -1.
print("str3 present in str2 at index : ", str2.find(str3))

str4 = "i am satish"
sks = str4.replace(" ", "@")  # space ko @ se replace kardo in string str4
print("str4 after replacing : ", sks)


if (str2.find(str3) >= 0):  # or if (str3 in str2):
    print("str3 is present in str2")
else:
    print("str3 is absent in str2")

for i in str4:
    print("str4 : ", str4)

str5 = "SatIsh kuMaR ShAh"
str5 = str5.upper()
print("str5 in UpperCase : ", str5)
str5 = str5.lower()
print("str5 in lowercase : ", str5)
