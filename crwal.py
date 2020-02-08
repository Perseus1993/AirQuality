import requests
from bs4 import BeautifulSoup
import bs4
import re
import json
from pyecharts import Map, Geo

aqilist = []   # 储存城市AQI
clist = []     # 储存城市链接
cnlist = []    # 储存城市名字
cwlink = []   # 异常链接


def get_all_city():    # 爬取
    url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 伪装成浏览器，headers
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("失败")
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
    area_information = json.loads(area_information.group(0))

    cities = []
    nums = []

    for area in area_information:
        for city in area['cities']:
            print(city['cityName'] + '确诊',city['confirmedCount'])
            cities.append(city['cityName'])
            nums.append(city['confirmedCount'])
            print("----")
        print("****************************************************************")

    geo = Geo("全国", "data", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')

    # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
    geo.add("肺炎", cities, nums, type="scatter", symbol = "circle" ,is_random=True, effect_scale=10, visual_range=[0, 200],visual_text_color="#fff",
        trail_length = 0.4 ,symbol_size=10, is_visualmap=True, is_roam=True,geo_normal_color="#323c48",geo_emphasis_color='#2a033d')
    geo.render(path="./肺炎.html")


def main():
    get_all_city()


main()
