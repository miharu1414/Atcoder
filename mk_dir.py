import os
import shutil


file_name = input("フォルダ名を指定してください")
if "ABC" in file_name:
    new_dir_path = "./AtCoder/ABC/" + file_name
elif "ARC" in file_name:
    new_dir_path = "./AtCoder/ARC/" + file_name
try:
    os.mkdir(new_dir_path)
except FileExistsError:
    print("フォルダが既にあります")
    import shutil
    # shutil.rmtree(new_dir_path)
    exit()
for i in range(6):
    path = new_dir_path+ "/" + chr(ord('a') + i)
    if i >= 0:
        src = './AtCoder/template.cpp'
        path1 = path + ".cpp"
        shutil.copyfile(src,path1)

    
    path2 = path + ".py"
    f = open(path2, 'w')
    f.write('')  # 何も書き込まなくてファイルは作成されました
    f.close()
    print(path)