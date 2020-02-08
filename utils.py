import os
# 文件计数

# 遍历文件夹
def walkFile(file):
    count = 0
    csv_paths = [] #存储csv文件们的路径
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            count += 1
            print(os.path.join(root, f))
            csv_paths.append(os.path.join(root, f))

        # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))
    return (csv_paths, count)
