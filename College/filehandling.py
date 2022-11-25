
# 1st Method

# # how to open a file
# f = open('College/data.txt')
# '''By default our file is open in read mode.'''

# '''
# if this above file data.txt was in some other folder than we have used the following code below :
# open('folder_name/file_name')
# In the above case file name is data.txt
# open('folder_name/data.txt')
# '''

# '''
# # To open file in read mode
# open('data.txt', 'r')  # or open('data.txt')

# # To open file in write mode
# open('data.txt', 'w')
# '''

# '''
# print(f.readline())  # using this first line read ho jaayegi
# print(f.readline())  # next line(2nd line) will be read
# print(f.readline())  # third line will be read
# '''

# # To read file in one go
# for line in f:
#     print(line)

# # we always have to close file after opening it.

# # how to close the file
# f.close()

'''
In the above method we have to close the file by f.close(). 
If there is any error then the file will not close and this is expensive.
And the above method is not recommended.
'''

# 2nd Method(this method is guaranteed that it will close the file). The with keyword will automatically close the file.
'''Even there is an error even then the file will be closed.'''
with open('College/data.txt') as f:
    # for line in f:
    #     print(line)

    # f.read() will read the whole file.
    # print(f.read())

    # To read 10 characters from the file.
    print(f.read(10))
    print(f.read(10))  # next 10 characters will be read.
    f.seek(0)  # pointed to 0th index.
    '''again first 10 characters will be read again because we have pointed the cursor towards index 0 using seek.'''
    print(f.read(10))


# Writing in a File
data = ['Satish\n', 'Nitesh\n', 'Major\n']
with open('College/new_file.txt', 'w') as f:
    f.write('Satish\n')
    f.writelines(data)
