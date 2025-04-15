import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# === 准备工作 ===
# 需要安装的库：
# pip install jieba wordcloud matplotlib pillow

# === 第一步：读取文本 ===
try:
    with open('DeepSeek.txt', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print("未找到文件 hot_time.txt，请检查文件路径")
    exit()

# === 第二步：加载停用词 ===
def load_stopwords():
    """从文件加载停用词，若无文件则使用默认停用词"""
    try:
        with open('stopwords.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("未找到停用词文件，使用默认停用词")
        return ['的', '了', '是', '在', '和', '就', '都', '这', '有', '我', '你']

stopwords = load_stopwords()

# === 第三步：中文分词处理 ===
# 使用jieba进行精确模式分词
words = jieba.lcut(text)

filtered_words = [word for word in words if len(word) > 1 and word not in stopwords]

# === 第四步：生成词频统计 ===
word_counts = Counter(filtered_words)
top_words = word_counts.most_common(100)  # 取前100个高频词

# === 第五步：配置词云 ===
wc = WordCloud(
    font_path='msyh.ttc',      # 中文字体文件路径（Windows系统微软雅黑路径，Mac/Linux需替换为系统字体路径）
    width=800,                 # 图片宽度
    height=600,                # 图片高度
    background_color='white',  # 背景颜色
    max_words=80,             # 最大显示词数
    colormap='viridis',        # 配色方案
    contour_width=1,           # 轮廓宽度
    contour_color='steelblue'  # 轮廓颜色
)

# === 第六步：生成词云 ===
# 从词频字典生成词云
wordcloud = wc.generate_from_frequencies(dict(top_words))

# === 第七步：显示和保存 ===
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 隐藏坐标轴

# 显示图片
plt.show()

# 保存图片
wordcloud.to_file('wordcloud_output.png')
print('词云已保存为 wordcloud_output.png')