# 全国122个城市历史空气质量数据及代码

## 背景

阿里巴巴与IJCAI联合举办的[口碑商家流量预测](https://tianchi.shuju.aliyun.com/competition/introduction.htm?spm=0.0.5678.0.F7TTMW&raceId=231591)需要使用天气信息，所以爬取了相关城市的历史空气质量（AQI）数据。

## 数据来源

数据来源于这里：https://www.aqistudy.cn/historydata/index.php

## 数据格式
一个城市的数据是一个csv文件，文件中有2列，第1列为日期，如“2015-10-10”,第2列为空气质量数据。
由于空气质量数据范围包括很多，我们只爬取了aqi综合数据，其他数据可以用提供的代码扩展。

## 数据范围
日期范围：2015-07-01至2016-11-31,每天的数据。

## 城市列表

城市列表见city.txt文件。

所有数据请见aqi文件夹，每个城市一个文件。

alldata.csv将所有城市数据保存到了一个。

## 源码支持

源码用Python写的,见crawl_aqi.py文件，比较好扩展。

## 缺失数据

目前缺失了**天门**和**思茅**两地的数据。在另一个网站上找到了它们2016年6月以后的天气数据，其他月份用了湖北省和云南省几个城市数据平均做为它们的数据。