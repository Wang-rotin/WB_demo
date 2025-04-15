import paddlehub as hub
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list1 = []
res = cursor.execute("select time from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list1.append(j)
print(list1)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# # 读取数据
# list2 = []
# res = cursor.execute("select href from app01_ershida_search")
# for i in cursor.fetchall():
#     for j in i:
#         list2.append(j)
# print(list2)
# # 提交事务
# conn.commit()
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()
#
# conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='wdl_01', charset='utf8')
#
# # 建立游标
# cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list3 = []
res = cursor.execute("select author from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list3.append(j)
print(list3)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list4 = []
res = cursor.execute("select content from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list4.append(j)
print(list4)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list5 = []
res = cursor.execute("select share_num from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list5.append(j)
print(list5)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list6 = []
res = cursor.execute("select comment_num from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list6.append(j)
print(list6)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list7 = []
res = cursor.execute("select like_num from app01_deepseek")
for i in cursor.fetchall():
    for j in i:
        list7.append(j)
print(list7)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()


senta = hub.Module(name="senta_lstm")
test_text = list4
results = senta.sentiment_classify(texts=test_text)
nums = [[] * 2 for i in range(5000)]

jiji=0
zhongxing=0
xiaoji=0

for result in results:
    print(result['text'])
    print(result['sentiment_label'])
    print(result['sentiment_key'])
    # print(type(result['sentiment_key']))
    print(result['positive_probs'])
    print(result['negative_probs'])
    #
    if result['positive_probs']>0.6:
        jiji+=1
        nums[0].append('积极')
    elif result['positive_probs']>0.4:
        zhongxing+=1
        nums[0].append('中性')
    else:
        xiaoji+=1
        nums[0].append('消极')


    # nums.append(result['text'])
    # nums.append(result['sentiment_label'])
    # nums[0].append(result['sentiment_key'])
    nums[1].append(result['positive_probs'])
    # print(nums)
    # nums.append(result['negative_probs'])
print(jiji)
print(zhongxing)
print(xiaoji)

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# # 建立游标
cursor = conn.cursor()

# # 数据库操作
# # (1)定义一个格式化的sql语句

sql = 'insert into app01_feel_analyse2(jiji,zhongxing,xiaoji,num,key_s, time,author, content, share_num, comment_num, like_num) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# # 读取数据
for i in range(len(nums)):
    data = (jiji,zhongxing,xiaoji,nums[1][i],nums[0][i],list1[1],list3[i],list4[i],list5[i],list6[i],list7[i])
    # data = (nums[0][i], nums[1][i])
    # data = (nums[i], list4[i],)
    try:
        cursor.execute(sql, data)
        conn.commit()
    except Exception as e:
        print('插入数据失败', e)
        conn.rollback()  # 回滚
#
# # 关闭游标
cursor.close()
#
# # 关闭连接
conn.close()
