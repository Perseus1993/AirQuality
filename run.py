from utils import *
from ex import *
import os
cvs_paths = []
from matplotlib import pyplot as plt

#
# cvs_paths, sum = walkFile("C:\\Users\\86158\\Desktop\\air_data\\city")
# test_paths = 'C:\\Users\\86158\\Desktop\\air_data\\city\\城市_20150101-20151231\\china_cities_20150103.csv'


# count = 0
# for path in cvs_paths:
#     count += 1
#     print('处理第', count,'/',sum,'个文件')
#     os.system("cls")
    # get_pm2(path)
avg_paths, sum = walkFile("C:\\Users\\86158\\Desktop\\air_data\\out_put_city")
test_av_path = 'C:\\Users\\86158\\Desktop\\air_data\\out_put_city\\20140514.csv'

data_tj = []
data_sy = []
data_sjz = []
data_sh = []
data_dl = []

for path in avg_paths:
    print(path)
    data2 = get_pm2_every(path , '天津', "2018-12-30", "2020-03-01")
    data3 = get_pm2_every(path , '三亚', "2018-12-30", "2020-03-01")
    data4 = get_pm2_every(path , '石家庄', "2018-12-30", "2020-03-01")
    data5 = get_pm2_every(path , '上海', "2018-12-30", "2020-03-01")
    data6 = get_pm2_every(path , '大连', "2018-12-30", "2020-03-01")

    if(data2 is not None):
        for it in data2:
            data_tj.append(it)
    if(data3 is not None):
        for it in data3:
            data_sy.append(it)
    if(data4 is not None):
        for it in data4:
            data_sjz.append(it)
    if(data5 is not None):
        for it in data5:
            data_sh.append(it)
    if(data6 is not None):
        for it in data6:
            data_dl.append(it)


print('done')

for data in (data_tj,data_sy,data_sjz,data_sh,data_dl):
    sy = [0,0,0,0,0,0,0]
    for it in data:
        if(it < 12):
            sy[0] += 1
        elif(it < 35):
            sy[1] += 1
        elif(it < 55):
            sy[2] += 1
        elif(it < 150):
            sy[3] += 1
        elif(it < 250):
            sy[4] += 1
        elif(it < 500):
            sy[5] += 1
    print(sy)
x = range(0, len(data))
plt.plot(x , data_tj,label = '天津')
plt.plot(x , data_sy, label = '三亚')
plt.plot(x , data_sjz, label = '石家庄')
plt.plot(x , data_sh, label = '上海')
plt.plot(x , data_dl, label = '大连')

plt.xlabel('小时')
plt.ylabel('PM2.5浓度-微克每立方米 ')
plt.title('2019.1.1到2020.2.1每小时PM2.5浓度示意图')
plt.legend(loc = 2)
plt.show()




# tj = [0,0,0,0,0,0,0]
# for it in data:
#     if(it < 12):

# sy = [0,0,0,0,0,0,0]
# for it in dataS:

# print(tj)
# print(sy)
