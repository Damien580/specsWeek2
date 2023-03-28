# How to create and write a file in .py:

# f = open("practice.txt", "w+") # filename.filetype, "w+"=write plus
# f.write("This is a test string")
# f.close()




import os
# print(os.getcwd())
# print(os.listdir("/Users/damienredd/School/DevMountain/Python F35/week 2/py-proj-2"))




import shutil
# shutil.move('practice.txt', "/Users/damienredd/School/DevMountain/Python F35/week 2/py-proj-2")



# "pip install send2trash" is a delete file module that does NOT permanently delete files, but sends them to the trash instead!!!
# enter pip install send2trash in the terminal to install it

import send2trash
# print(os.listdir())

# send2trash.send2trash('practice.txt')

# print(os.getcwd())
# for folder, sub_folders, files in os.walk('/Users/damienredd/DevMountain/Python 35/week 2/py-proj-2/starter'):
#     print(f"Currently looking at {folder}")
#     print("\n")
#     print("the subfolders are: ")
#     for sub_fold in sub_folders:
#         print(f"\tSubfolder: {sub_fold}")
        
#     print("\n")
#     print("the files are: ")
#     for f in files:
#         print(f"\tFile: {f}")
#     print("\n")
    
# print(os.walk('/Users/damienredd/DevMountain/Python 35/week 2/py-proj-2/starter'))



