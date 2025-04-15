import parsel
import requests
import re
from lxml import etree

# 创建 TXT 文件用于写入数据
with open('yaowen.txt', 'a', encoding='utf-8') as f:
    # 请求 URL
    url = 'https://s.weibo.com/top/summary?cate=socialevent'

    # 请求头部伪装
    headers = {
        'cookie':' SCF=Apixvw8BdRGwzbUbuj1dq5SaIfgdPXANBWVf8DZONQJL0Lf4rQxUgpZzDoAjZT_z6TMa536TtbOKaDyUv1DUO7w.; SINAGLOBAL=7108719522516.833.1737884519818; UOR=,,tophub.today; ALF=1745323699; SUB=_2A25K24njDeRhGeFG7FMX9CfJzDuIHXVpmIMrrDV8PUJbkNANLVTHkW1NeOBlo0isPkKunJOOQE-h_vuywqUaPq1i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_RK_F.HG_xN923UpJsqoZ5JpX5KMhUgL.FoMRS02cSh.fS0M2dJLoIEYLxKBLBonL1h.LxKBLBonL1h.LxK-L1K2L1K5LxK-L1K2L1K5LxK-L1K2L1K50e7tt; _s_tentry=-; Apache=6276342665704.562.1743326568332; ULV=1743326568338:10:6:1:6276342665704.562.1743326568332:1742986193567',
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

    # 遍历提取的元素并存储
    for i in range(0, len(title)):
        # 获取排名
        rank = i + 1

        # 获取链接
        hf = 'https://s.weibo.com' + href[i]

        # 获取标题
        hot_title = title[i]

        # 清理热度数据，去除非数字字符
        new_num = re.sub('\D', '', num[i]) if num[i] else '0'

        # 构造写入 TXT 的格式
        txt_line = f"排名: {rank}, 标题: {hot_title}, 热度: {new_num}, 链接: {hf}\n"

        # 将当前行写入 TXT 文件
        f.write(txt_line)

print("数据已成功保存到 yaowen.txt 文件中。")
