# 疫情可视化01

原本的想法是找到各大发热门诊的患者数量，批量产生GPS整合到全国地图，后来发现没有统一数据的网站，只有腾讯，丁香医生等有每个地级市的数据

##数据爬取

数据来自<a href = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'>丁香医生</a>

分析网页，发现返回的数据是静态的，大喜，省事不少。直接request.get

首先分析返回的信息，发现具体城市的数据都在 <script id="getListByCountryTypeService1">下面

```python

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
```
##可视化

使用pyecharts 下面的 geo。我把上限都设为了200，当单个城市数据大于200时候都变成了最深色

```python
geo = Geo("全国", "data", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')

  # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
  geo.add("肺炎", cities, nums, type="scatter", symbol = "circle" ,is_random=True, effect_scale=10, visual_range=[0, 200],visual_text_color="#fff",
      trail_length = 0.4 ,symbol_size=10, is_visualmap=True, is_roam=True,geo_normal_color="#323c48",geo_emphasis_color='#2a033d')
  geo.render(path="./肺炎.html")

```
