from pyecharts import Map, Geo
import pandas as pd
import numpy as np

# 读取csv文件
df = pd.read_csv('res.csv')
# 空气质量评分
indexs = list(df)[3:]
values = np.array(df.iloc[0]).tolist()[3:]

print(indexs)

print(values)

geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center", width=2400, height=1200, background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("空气质量评分", indexs, values, type="scatter", symbol = "circle" ,is_random=True, effect_scale=10, visual_range=[0, 200],visual_text_color="#fff",
    trail_length = 0.4 ,symbol_size=30, is_visualmap=True, is_roam=True,geo_normal_color="#323c48",geo_emphasis_color='#2a033d')
geo.render(path="./空气.html")
