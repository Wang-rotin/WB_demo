import parsel
import csv
import requests
import pandas as pd
import re
import mysql.connector
from lxml import etree

# 创建 CSV 文件用于写入数据
with open('res.csv', 'a', encoding='utf-8', newline='') as f:
    # 定义 CSV 的列名
    csv_writer = csv.DictWriter(f, fieldnames=['排名', '标题', '热度', '链接'])

    # 写入表头
    csv_writer.writeheader()

    # 请求 URL
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'

    # 请求头部伪装
    headers = {
        'cookie': 'SCF=Apixvw8BdRGwzbUbuj1dq5SaIfgdPXANBWVf8DZONQJL0Lf4rQxUgpZzDoAjZT_z6TMa536TtbOKaDyUv1DUO7w.; SINAGLOBAL=7108719522516.833.1737884519818; UOR=,,tophub.today; ALF=1745323699; SUB=_2A25K24njDeRhGeFG7FMX9CfJzDuIHXVpmIMrrDV8PUJbkNANLVTHkW1NeOBlo0isPkKunJOOQE-h_vuywqUaPq1i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_RK_F.HG_xN923UpJsqoZ5JpX5KMhUgL.FoMRS02cSh.fS0M2dJLoIEYLxKBLBonL1h.LxKBLBonL1h.LxK-L1K2L1K5LxK-L1K2L1K5LxK-L1K2L1K50e7tt; _s_tentry=-; Apache=6276342665704.562.1743326568332; ULV=1743326568338:10:6:1:6276342665704.562.1743326568332:1742986193567',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    # 请求数据
    response = requests.get(url, headers=headers)

    # 使用 lxml 的 etree 解析 HTML 内容
    html = etree.HTML(response.text)

    # 使用 XPath 提取标题和链接
    href = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a/@href')
    title = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a/text()')

    # 使用 parsel 提取热度数据
    trs = parsel.Selector(response.text).css('#pl_top_realtimehot tbody tr')
    num = []

    # 提取热度信息
    for tr in trs:
        hot = tr.css('.td-02 span::text').get()
        if hot:
            num.append(hot)
        else:
            num.append('0')

    # 初始化存储数据的列表
    rank = []
    hot_href = []
    hot_title = []
    hot_num = []

    # 遍历提取的元素并存储
    for i in range(0, len(title)):
        rank.append(i + 1)
        hf = 'https://s.weibo.com' + href[i]
        hot_href.append(hf)
        hot_title.append(title[i])

        # 清理热度数据，去除非数字字符
        new_num = re.sub('\D', '', num[i]) if num[i] else '0'
        hot_num.append(new_num)

# 将数据存储到 MySQL 数据库中
try:
    # 连接数据库
    conn = mysql.connector.connect(
        host='127.0.0.1',  # MySQL 主机（本地）
        user='root',  # MySQL 用户名
        password='123456',  # MySQL 密码
        database='project'  # MySQL 数据库名称
    )

    cursor = conn.cursor()

    # 删除数据库表格中的所有数据
    cursor.execute("DELETE FROM app01_hot_rank")

    # 插入数据到数据库
    for i in range(len(rank)):
        cursor.execute(
            "INSERT INTO app01_hot_rank (`rank`, hot_href, hot_title, hot_num) VALUES (%s, %s, %s, %s)",
            (rank[i], hot_href[i], hot_title[i], hot_num[i])
        )

    # 提交事务
    conn.commit()

    print(f"成功插入 {len(rank)} 条数据到数据库")

except mysql.connector.Error as err:
    print(f"数据库连接失败：{err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
