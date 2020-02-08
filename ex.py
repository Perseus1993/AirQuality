# 导入pandas包
import pandas as pd
import numpy as np
import os

out_put_dir = 'C:\\Users\\86158\\Desktop\\air_data\\out_put_city'

def get_pm2(path):

    #有无效文件ds.store
    if(path.split('.')[-1] != 'csv'):
        print('无效文件ds.store')
        return
    # 读取csv文件
    df = pd.read_csv(path)
    print(path)

    # 获得输出路径
    filename = path.split('\\')[-1].split('_')[-1]
    out_path = os.path.join(out_put_dir, filename)

    df = df.loc[df["type"].str.endswith('PM2.5'), :]



    # df = df.iloc[:, 3:]


    # print(list(df))



    # print(np.array(df.iloc[0]).tolist())

    df.to_csv(out_path, index=False)
    print("**解析完毕**")

    # print(df.loc[(df["Supplier Name"].str.contains('Z'))|(df['Cost'].str.strip('$').astype(float) > 600.0),:])

    # df.to_csv("res2.csv",index=None)
