# 导入pandas包
import pandas as pd
import numpy as np

# 读取csv文件
df = pd.read_csv('res.csv')

# 显示前10行数据
# print(df.head(1))


# df2 = df.loc[df["type"].str.endswith('PM2.5'), :]
# print(df2)

df = df.iloc[:,3:]

print(list(df))
print(np.array(df.iloc[0]).tolist())

# print(df[df['Cost'].str.strip('$').astype(float) > 600])
# print(df.loc[(df["Supplier Name"].str.contains('Z'))|(df['Cost'].str.strip('$').astype(float) > 600.0),:])

# df.to_csv("res2.csv",index=None)
