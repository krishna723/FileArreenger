import os
import glob
s=input("Enter the path:")
file_list=glob.glob(s+"/*.*")
extension_set=set()
for file in file_list:
    extension=file.split(".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue
def creat_dir():
    for dir in extension_set:
        try:
            os.mkdir(s+"/"+dir + "_file")
        except FileExistsError:
            continue

def arrange():
    for file in file_list:
        file_name=os.path.basename(file)
        fextension=file.split(".")
        try:
            os.rename(file,s+"/"+fextension[1]+"_file/"+file_name)
        except(OSError,IndexError):
            continue
creat_dir()
arrange()

