import requests
from bs4 import BeautifulSoup
import bs4

aqilist = []   # 储存城市AQI
clist = []     # 储存城市链接
cnlist = []    # 储存城市名字
cwlink = []   # 异常链接


def get_one_page(city):   # 获得HTML 爬取城市信息
    url = "http://www.air-level.com"+city
    if city in cwlink:
        aqilist.append("异常链接")
    else:
        try:
            kv = {'user-agent': 'Mozilla/5.0'}  # 伪装成浏览器，headers
            r = requests.get(url, headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except:
            print("爬取失败")
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        s = soup.find("span")
        aqilist.append(s.string)


def get_all_city():    # 爬取城市链接
    url = "http://www.air-level.com"
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 伪装成浏览器，headers
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("爬取城市链接失败")
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    time = soup.find('h4').string
    print(time)
    for it in soup.find(id="citylist").children:
        if isinstance(it, bs4.element.Tag):   # 检测it的类型，得是一个bs4.element.Tag类型
            for its in it.find_all('a'):
                clist.append(its.get('href'))  # 加入列表当中去
                cnlist.append(its.string)


def main():
    get_all_city()
    print("共爬取了{}个城市".format(len(clist)))
    for it in range(len(clist)):
        get_one_page(clist[it])
        print("{} {}".format(cnlist[it], aqilist[it]))


main()
