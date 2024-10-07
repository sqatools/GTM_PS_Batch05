import glob
import os

# for file in glob.glob(fr"E:\Filesdata\batch05\*"):
#     print(file)


files = glob.glob(fr"E:\Filesdata\batch05\*")
latest_file = max(files, key=os.path.getmtime)
print(latest_file)
