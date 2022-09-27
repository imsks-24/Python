# Questions
# 1. Problem : In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format : The first line of input contains the original string. The next line contains the substring.
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# 2.https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem : Consider a list (list = []). You can perform the following commands:

# 1.insert i e: Insert integer  at position .
# 2.print: Print the list.
# 3.remove e: Delete the first occurrence of integer .
# 4.append e: Insert integer  at the end of the list.
# 5.sort: Sort the list.
# 6.pop: Pop the last element from the list.
# 7.reverse: Reverse the list.
# 8.Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example:
# N = 4
# append 1
# append 2
# insert 3 1
# print
# • append 1: Append 1 to the list, arr = [1] .
# • append 2: Append 2 to the list, arr = [1, 2] .
# • insert 3 1: Insert 3 at index 1, arr = [1, 3, 2] .
# • print: Print the array .

# Output:
# [1, 3, 2]

# Sample Input 0 :

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0 :

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


def insertintoList(l, x, y):  # x ki position pe y ko store karwaana hai list l ke andar
    l.insert(x, y)


if __name__ == '__main__':
    N = int(input())
    l = []  # empty list
    for i in range(N):
        inp = input()
        if (inp.find("insert") >= 0):  # inp is a string
            a = inp[7:]  # 7th string se 0 start hai check sample input
            x, y = a.split()  # 1st wala element x mai chala jaayega & 2nd waala y mai
            x = int(x)  # converted to integer
            y = int(y)  # converted to integer
            insertintoList(l, x, y)

        elif (inp.find("print") >= 0):
            print(l)

        elif (inp.find("remove") >= 0):
            b = inp[7:]  # check sample input
            b = int(b)  # converted into integer
            l.remove(b)  # we can make function alse
        elif (inp.find("append") >= 0):
            c = inp[7:]
            c = int(c)
            l.append(c)
        elif (inp.find("sort") >= 0):
            l.sort()
        elif (inp.find("pop") >= 0):
            l.pop(-1)  # last element ko delete kar rhe hai question mai diya hai
        elif (inp.find("reverse") >= 0):
            l.reverse()
        elif (inp.find("print") >= 0):
            print(l)
