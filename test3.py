#encoding=utf-8
from bs4 import BeautifulSoup
import requests
import bs4
import eventlet
eventlet.monkey_patch()

aqilist = []   # 储存城市AQI
clist = []     # 储存城市链接
cnlist = []    # 储存城市名字
cwlink = []   # 异常链接

def get_city_name():
    url = "http://www.air-level.com"
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("爬取城市链接失败")

    # print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    time = soup.find('h4').string
    # print(time)
    # print(soup.find(id = "citylist"))
    for it in soup.find(id = "citylist").children:
        if isinstance(it, bs4.element.Tag): # 检测it的类型，得是一个bs4.element.Tag类型
            for its in it.find_all('a'):
                clist.append(its.get('href'))  # 加入列表当中去
                cnlist.append(its.string)

def get_data(city):
    with eventlet.Timeout(2,False):
        url = "http://www.air-level.com" + city
        if city in cwlink:
            aqilist.append("异常链接")
        else:

            try:
                kv = {'user-agent': 'Mozilla/5.0'}
                r = requests.get(url, headers=kv)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
            except:
                print("爬取失败")            
            # s = soup.find("span")
            # aqilist.append(s.string)
            try:
                demo = r.text
                soup = BeautifulSoup(demo, "html.parser")
                s = soup.find("table")
                for ss in s.children:
                    if isinstance(ss, bs4.element.Tag):
                        count = 0
                        str = []
                        for sss in ss.find_all("td"):
                            str.append(sss.string)
                            count += 1
                            if(count == 2):
                                break
                        if(str != []):
                            print(str)


                        print("*************")
            except:
                print("发生错误")




def test():
    url = "http://www.air-level.com/air/anshan/"
    if 1 == 2:
        aqilist.append("异常链接")
    else:
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except:
            print("爬取失败")
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        s = soup.find("table")
        for ss in s.children:
            print("children")
            if isinstance(ss, bs4.element.Tag):
                count = 0
                str = []
                for sss in ss.find_all("td"):
                    str.append(sss.string)
                    count += 1
                    if(count == 2):
                        break
                if(length(str) == 2):
                    print(str)
                    print("*************")

def main():
    get_city_name()
    print("共爬取了{}个城市".format(len(clist)))
    for it in range(len(clist)):
        get_data(clist[it])
        # print("{} {}".format(cnlist[it], aqilist[it]))
    # test()


main()
