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

# 存储微博数据app01_tiyusaishi_result
weibo_data = []

# MySQL连接设置
db_config = {
    'host': '127.0.0.1',  # 数据库主机
    'user': 'root',       # 数据库用户名
    'password': '123456',  # 数据库密码
    'database': 'project',  # 数据库名称
    'port': 3306  # MySQL端口，默认是3306
}

try:
    # 连接到 MySQL 数据库
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 删除表格中的旧数据
    cursor.execute("DELETE FROM app01_wanhui_315")
    print("成功删除旧数据")

    # 设置固定话题
    topic = "315晚会"
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

                # 插入数据到数据库
                cursor.execute(
                    "INSERT INTO app01_wanhui_315 (time, author, content, share_num, comment_num, like_num) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (times,nick_name, contents, zf, pl, dz)
                )
            except Exception as e:
                print(f"提取微博信息时发生错误: {e}")

    # 提交事务
    conn.commit()
    print(f"成功插入数据到数据库")

except mysql.connector.Error as err:
    print(f"数据库连接失败：{err}")

finally:
    # 关闭连接
    cursor.close()
    conn.close()
    driver.quit()
