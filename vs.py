from utils import *
import matplotlib.pyplot as plt

category_names = ['优', '良','轻度污染', '中度污染', '重度污染','严重污染']
results = {
    '天津': [456, 2886, 2558, 2847, 443, 62, 0],
    '三亚': [4522, 4402, 260, 14, 0, 0, 0],
    '石家庄': [281, 3174, 2089, 2579, 958, 167, 0],
    '上海': [761, 4792, 1816, 1818, 61, 0, 0],
    '大连': [1312, 4911, 1351, 1436, 219, 20, 0]
}

survey(results, category_names)
plt.title('2019.1.1到2020.2.1的PM2.5浓度级别比例图')
plt.legend(loc = 2, bbox_to_anchor = (1, 0))
plt.show()
