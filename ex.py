# 导入pandas包
import pandas as pd
import numpy as np
import os

out_put_dir = 'C:\\Users\\86158\\Desktop\\air_data\\out_put_city'
# 错误日志路径
err_log_dir = 'C:\\Users\\86158\\Desktop\\air_data\\err_log.txt'

# 从原始数据提取出pm2.5
def get_pm2(path):
    try:
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

        df.to_csv(out_path, index=False)
        print("**解析完毕**")

    except Exception as err:
            f = open(err_log_dir, 'w+')
            f.writelines(path)
            f.writelines("\n")
            f.close()

def get_pm2_avrage(path, city_name, start_date, end_date):
    try:
        #有无效文件ds.store
        if(path.split('.')[-1] != 'csv'):
            print('无效文件ds.store')
            return
        # 读取csv文件
        # 筛选日期
        
        df = pd.read_csv(path)
        print(path)
        print(df[city_name])

    except Exception as err:
            f = open(err_log_dir, 'w+')
            f.writelines(path, "  get_pm2_avrage")
            f.writelines("\n")
            f.close()
