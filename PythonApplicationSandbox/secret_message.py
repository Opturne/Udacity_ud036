import os

def rename_files():
    dir_path = r"C:\Users\abarruol\Downloads\python\prank"
    file_list = os.listdir(dir_path)
    print (file_list)

    for file_name in file_list:
        os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, file_name.lstrip("0123456789")))

rename_files()