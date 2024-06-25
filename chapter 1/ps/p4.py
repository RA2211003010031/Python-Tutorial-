# importing the "os" module
import os 

# selecting the path/directory
path = "/"

# putting the directory list in dir_list container/variable
dir_list = os.listdir(path)

# printing the result
print("Files and directories in " ", path, " " :")
print(dir_list)