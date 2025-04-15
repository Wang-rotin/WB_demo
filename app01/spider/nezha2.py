import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse

# 设置 ChromeDriver 路径
chrome_driver_path = r'E:\Project\first\chromedriver.exe'
service = Service(chrome_driver_path)

# 设置 Chrome 浏览器选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 如果你想在后台运行，不显示浏览器窗口
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 创建浏览器实例
driver = webdriver.Chrome(service=service, options=chrome_options)

# 存储微博数据
weibo_data = []

# 设置固定话题
topic = "哪吒2票房"
key = urllib.parse.quote(topic)  # URL 编码
new_url = f'https://s.weibo.com/weibo?q=%23{key}%23'
print(f"新微博链接: {new_url}")  # 打印生成的新微博链接
driver.get(new_url)

# 等待微博页面加载
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pl_topic_header"]/div[1]/div[2]/div[1]//h1//a'))
)

# 提取微博标题
title_element = driver.find_element(By.XPATH,
                                    '//*[@id="pl_topic_header"]/div[1]/div[2]/div[1]//h1//a')
title = title_element.text
print(f"微博标题: {title}")

# 打开txt文件进行写入
with open("nezha2.txt", "w", encoding="utf-8") as f:
    f.write(f"微博标题: {title}\n\n")

    # 爬取前5页微博内容
    for page in range(1, 6):  # 修改为爬取前5页
        print(f"正在爬取第 {page} 页")
        if page > 1:
            # 如果不是第一页，更新 URL 以获取下一页
            driver.get(f"{new_url}&page={page}")

        # 等待页面加载
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, './/div[@action-type="feed_list_item"]'))
        )

        # 提取微博信息
        divs = driver.find_elements(By.XPATH, './/div[@action-type="feed_list_item"]')
        for div in divs:
            try:
                # 提取时间、作者、内容等信息
                times = div.find_element(By.XPATH, './/div[@class="from"]/a[1]').text
                nick_name = div.find_element(By.XPATH,
                                             './/div[@class="content"]/div[@class="info"]/div[2]/a').get_attribute(
                    'nick-name')
                comment_url = div.find_element(By.XPATH, './/div[@class="from"]/a').get_attribute('href')
                contents = div.find_element(By.XPATH, './/p[@node-type="feed_list_content"]').text

                # 提取转发、评论和点赞数量
                zf = div.find_element(By.XPATH, './/div[@class="card-act"]/ul/li[1]/a').text
                pl = div.find_element(By.XPATH, './/div[@class="card-act"]/ul/li[2]/a').text
                dz = div.find_element(By.XPATH,
                                      './/div[@class="card-act"]/ul/li[3]//span[@class="woo-like-count"]').text

                # 处理转发、评论和点赞数量
                zf = int(zf) if zf.isdigit() else 0
                pl = int(pl) if pl.isdigit() else 0
                dz = int(dz) if dz.isdigit() else 0

                # 打印提取的信息
                print(times, comment_url, nick_name, contents, zf, pl, dz)

                # 写入数据到txt文件
                # f.write(f"时间: {times}\n")
                # f.write(f"作者: {nick_name}\n")
                f.write(f"{contents}\n")
                # f.write(f"转发数: {zf}, 评论数: {pl}, 点赞数: {dz}\n")
                # f.write(f"评论链接: {comment_url}\n\n")
            except Exception as e:
                print(f"提取微博信息时发生错误: {e}")

# 关闭浏览器
driver.quit()
print(f"成功爬取数据并保存到 nezha2.txt 文件中")
