from utils import *
from ex import *
import os
cvs_paths = []

cvs_paths, sum = walkFile("C:\\Users\\86158\\Desktop\\air_data\\city")
# test_paths = 'C:\\Users\\86158\\Desktop\\air_data\\city\\城市_20150101-20151231\\china_cities_20150103.csv'
count = 0
for path in cvs_paths:
    count += 1
    print('处理第', count,'/',sum,'个文件')
    os.system("cls")
    get_pm2(path)

# for path in cvs_paths:
#     get_pm2(path)
