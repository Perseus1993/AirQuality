import os
from dateutil.parser import parse
import numpy as np
import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 文件计数

# 遍历文件夹
def walkFile(file):
    count = 0
    csv_paths = [] #存储csv文件们的路径
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            count += 1
            print(os.path.join(root, f))
            csv_paths.append(os.path.join(root, f))

        # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))
    return (csv_paths, count)

def date_compare(str1, str2, date):
    # 输入日期格式 2017-04-30
    start_date = parse(str1)
    end_date = parse(str2)
    c=parse(str(date))

    if start_date < c < end_date:
        return True
    else:
        return False


def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('brg_r')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        # for y, (x, c) in enumerate(zip(xcenters, widths)):
        #     ax.text(x, y, str(int(c)), ha='center', va='center',
        #             color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
