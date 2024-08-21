import os
import shutil

"""
# get current working directory path
print(os.getcwd())
# E:\Trainings\GTM_PS_Batch05_1July2024\GTM_PS_Batch05\Deepesh\PythonProgramming\Python_OS_Module


# change working directory
os.chdir("E:\\Trainings\\GTM_PS_Batch05_1July2024\GTM_PS_Batch05\\Deepesh\\PythonProgramming")
print(os.getcwd())

# create a directory
#os.mkdir("NewFolder") # It will create folder in PythonProgramming directory.
os.chdir("E:\\Trainings\\GTM_PS_Batch05_1July2024\\GTM_PS_Batch05\\Deepesh\\PythonProgramming\\Python_OS_Module")
#os.mkdir("NewFolder1")


# remove directory
os.rmdir("NewFolder1")
"""

# create multi level directories
# s.makedirs("E:\\Filesdata\\batch05\\f1\\f2\\f3\\f4\\f5")

# rename folder name
# os.rename("E:\\Filesdata\\batch05\\f1", "E:\\Filesdata\\batch05\\TopDirectory")

# rename multiple folder directories
# os.renames("E:\\Filesdata\\batch05\\TopDirectory\\f2\\f3", "E:\\Filesdata\\batch05\\TopDirectory\\fold2\\fold3")

# get list of files and folders

file_folder_list = os.listdir("E:\\Filesdata")
print(file_folder_list)
print("total file/folder :", len(file_folder_list))  # 50

print("_" * 50)
# join two path:
file_path = os.path.join("E:\\Filesdata", "count_name.txt")
print("filepath :", file_path)  # True

# check the given path is file not
print(os.path.isfile("E:\\Filesdata\\count_name.txt"))  # True
print(os.path.isfile("E:\\Filesdata\\batch05"))  # False

# check the given path is folder or not
print(os.path.isdir("E:\\Filesdata\\batch05"))  # True


# get count of files and folder from target path

def get_file_folder_count(src_dir):
    files_list = []
    folder_list = []
    file_folder_list = os.listdir(src_dir)
    for val in file_folder_list:
        data_path = os.path.join(src_dir, val)
        if os.path.isfile(data_path):
            files_list.append(val)
        elif os.path.isdir(data_path):
            folder_list.append(val)

    print("Files count :", len(files_list))
    print("Folder count :", len(folder_list))


get_file_folder_count("E:\\Filesdata")

# copy files from one directory to another directory
print("_" * 50)
shutil.copy("E:\\Filesdata\\count_name.txt", "E:\\Filesdata\\batch05\\count_name.txt")
shutil.copy("E:\\Filesdata\\count_name.txt", "E:\\Filesdata\\batch05\\copy_count_name.txt")

# execute windows command via os module
# os.system("control")  # open control panel
# os.system("notepad.exe") # open fresh notepad
os.system("python first_program.py")  # execute the python file
os.system("dir E:\\Filesdata")  # get list of files and folders with dir command.
