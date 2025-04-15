import paddlehub as hub
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()

# 数据库操作
# (1)定义一个格式化的sql语句

# 读取数据
list1 = []
res = cursor.execute("select hot_title from app01_yule_rank")
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


list2 = []
res = cursor.execute("select hot_href from app01_hot_rank")
for i in cursor.fetchall():
    for j in i:
        list2.append(j)
print(list2)
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='project', charset='utf8')

# 建立游标
cursor = conn.cursor()


list3 = []
res = cursor.execute("select hot_num from app01_yule_rank")
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


senta = hub.Module(name="senta_lstm")
test_text = list1
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

sql = 'insert into app01_wenyu_result(jiji,zhongxing,xiaoji,num,key_s,title, hot_num,href) values(%s,%s,%s,%s,%s,%s,%s,%s)'
# # 读取数据
for i in range(len(nums)):
    data = (jiji,zhongxing,xiaoji,nums[1][i],nums[0][i],list1[i],list3[i],list2[i])
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
