
#* ================================================== *#
#* ================== File Hanlding ================= *#
#* ================================================== *#

# file = open('test.txt', 'w')
# file.write('Line 1')
# file.close()


#* ================================================== *#
#* ======== File Hanlding using `with` block ======== *#
#* ================================================== *#

# with open('test.txt', 'w') as file1:
#     file1.write('Line 1\n')

# `with` block will automatically close file
# no need to write `file.close()`


#* ================================================== *#
#* =================== Append mode ================== *#
#* ================================================== *#

# with open('test.txt', 'a') as file:
#     file.write('Line 2\n')
#     file.write('Line 3\n')
#     file.write('Line 4\n')


#* ================================================== *#
#* =================== Read mode ==================== *#
#* ================================================== *#

# with open('test.txt', 'r') as file:
#     # print(file.read()) # return file content in string
    
#     # print(file.readlines()) # return file content in list, every line is an item
    
#     print(file.readline()) # print first line in file
#     print(file.readline()) # print second line in file
    
#     print("I am reading lines of test.txt file")
#     print(file.readlines()) # print all remaining lines in file


#* ================================================== *#
#* ============= Read Limited Charactors ============ *#
#* ================================================== *#

# with open('test.txt', 'r') as file:
#     print(file.read(10)) # return only 10 charactors from file


#* ================================================== *#
#* =============== See Cursor Position ============== *#
#* ================================================== *#

# with open('test.txt', 'r') as file:
#     print(file.readline())
#     print("Cursor position:", file.tell())

#     print(file.readline())
#     print("Cursor position:", file.tell())


#* ================================================== *#
#* ============= Change Cursor Position ============= *#
#* ================================================== *#

# When we use write mode it truncates the file to zero length as soon as we open it.

# with open('test.txt', 'w') as file:
#     file.seek(0, 2) # we're seeking to the end of a file that is now empty — which is just position 0.
#     print(file.tell()) 
#     file.write("Line 5\n")

#* ================================================== *#

# with open('test.txt', 'r') as file:
#     file.seek(8)
#     print(file.read())


#* ================================================== *#
#* ================ Write & Read Mode =============== *#
#* ================================================== *#

# with open('test.txt', 'w+') as file:
#     file.write('Using w+ mode')
#     file.seek(0) # Change cursor position to start
#     print(file.read())


#* ================================================== *#
#* ================ Read & Append Mode ============== *#
#* ================================================== *#

# with open('test.txt', 'r+') as file:
#     print(file.read())
#     print("Cursor position:", file.tell())
#     file.write('Line 10\n')


#* ================================================== *#
#* ============= Difference between them ============ *#
#* ================================================== *#

# if file not exist and we try to use read mode, it will raise error

# with open('test1.txt', 'r') as file:
#     print(file.read()) #! Error: FileNotFoundError

# but if we use write mode it will create file 

# with open('test1.txt', 'w') as file:
#     file.write("Another line\n") # a new file 'test1.txt' created


#* ================================================== *#

# similar to this if you use 'r+' mode, and file not exist it will raise error,
# unline 'r+', 'w+' will create that file


# with open('test1.txt', 'r+') as file:
#     print(file.read()) #! Error: FileNotFoundError


