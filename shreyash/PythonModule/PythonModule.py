import os


##get current dirctory path
#print(os.getcwd())

##Change Working Directory
#print(os.chdir("C:\\PythonPractice\\GTM_PS_Batch05\\shreyash\\PythonModule"))
#print(os.getcwd())

##Create a Directory

#os.mkdir("New Folder")

##To remove Directory

#os.rmdir("New Folder")

##Create Multuple Directory

#os.makedirs("D:\\New folder\\Folder1\\Folder2")

##Rename the folder name/Multiple folder

#os.renames("D:\\New folder\\Folder1\\Folder2", "D:\\New folder\\Folder11\\Folder22")

##get list of files and folders:

#file_folder_list = os.listdir("D:\Software testing Course\De Clay Emporium _ Home_files")
#print(file_folder_list)
#print("total file/folder:", len(file_folder_list))

##Check the given path is file or not:

#print(os.path.isfile("D:\Software testing Course\De Clay Emporium _ Home_files"))

#print(os.path.isfile("D:\\Software testing Course\\De Clay Emporium _ Home_files\\4XLmdX1I4f31RzsJtpBKj(1)"))

##Check the given path is folder or not:

#print(os.path.isdir("D:\\Software testing Course\\De Clay Emporium _ Home_files"))
#print(os.path.isdir("D:\\Software testing Course\\De Clay Emporium _ Home_files\\4XLmdX1I4f31RzsJtpBKj(1)"))

##Get the count of files and folder from target path.

#files_list = []
#folder_list = []

#def get_file_folder_count(src_dir):
#    file_folder_list = os.listdir(src_dir)
#    for data in file_folder_list:
#        data_path = os.path.join(src_dir,data)
#        if os.path.isfile(data_path):
#            files_list.append(data)
#        elif os.path.isdir(data_path):
#            folder_list_append(data)
#    print("files count:", len(files_list))
#    print("folder count:",len(folder_list))
#get_file_folder_count("D:\\Software testing Course\\Python Lecture\\New folder")

##Copy Files from one dir to another dir:
import shutil

#shutil.copy("D:\\Software testing Course\\De Clay Emporium _ Home_files\\4XLmdX1I4f31RzsJtpBKj(1)","D:\\Software testing Course\\4XLmdX1I4f31RzsJtpBKj(1222)")

##Execute windows command via as module

#os.system("control")

#os.system("notepad.exe")

#os.system("pytho")

#os.system("dir D:\\Software testing Course\\De Clay Emporium _ Home_files\\4XLmdX1I4f31RzsJtpBKj")

