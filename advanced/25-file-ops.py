# Relative path of files used in this section:
# advanced/files/file1

# Open a files
openfile = open("files/file1", 'w')
openfile.write('My Sample Test File for Python Programming')
openfile.close()
openfile = open("files/file1", 'r')
print(openfile.read())

# Rename and Remove
import os
# os.rename("files/file2", "files/file4")
# os.remove("files/file3")

 os.mkdir("files/temp")
print(os.getcwd())
os.chdir("files")
print(os.getcwd())
os.rmdir("temp")

'''
Output:
-----------------------------------------------------------
My Sample Test File for Python Programming
C:\Users\ZeePC\PycharmProjects\Python-Training\advanced
C:\Users\ZeePC\PycharmProjects\Python-Training\advanced\files
'''