from django.db import models
from django.db.models import Max
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个主键
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    email = models.CharField(max_length=32)  # 邮箱



#######################################榜单########################################
#热搜榜单
class hot_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=2048, null=True)
    hot_num = models.CharField(max_length=64, null=True)

class HotRank(models.Model):
    rank = models.CharField(max_length=10, verbose_name="排名")
    hot_title = models.CharField(max_length=255, verbose_name="热搜标题")
    hot_href = models.URLField(max_length=2048, verbose_name="链接")
    hot_num = models.CharField(max_length=20, verbose_name="热度值")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#文娱榜
# class wenyu_rank(models.Model):
#      rank = models.CharField(max_length=64, null=True)
#      hot_title = models.CharField(max_length=64, null=True)
#      hot_href = models.CharField(max_length=2048, null=True)
#      hot_num = models.CharField(max_length=64, null=True)



class yule_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=2048, null=True)
    hot_num = models.CharField(max_length=64, null=True)


# 要闻榜
class yaowen_rank(models.Model):
     hot_title = models.CharField(max_length=64, null=True)
     hot_href = models.CharField(max_length=2048, null=True)

# 校园榜
class xiaoyuan_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=2048, null=True)
    hot_num = models.CharField(max_length=64, null=True)


# 体育榜
class tiyu_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=2048, null=True)
    hot_num = models.CharField(max_length=64, null=True)


# 游戏榜
class youxi_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=2048, null=True)
    hot_num = models.CharField(max_length=64, null=True)

######################################趋势分析话题#########################

class wanhui_315(models.Model):
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField( null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)

class nezha2(models.Model):
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)

class DeepSeek(models.Model):
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)


# 情感分析
class feel_analyse(models.Model):
    jiji=models.CharField(max_length=64, null=True)
    zhongxing=models.CharField(max_length=64, null=True)
    xiaoji=models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)
    href=models.URLField(max_length=2048, null=True)


class feel_analyse2(models.Model):
    jiji=models.CharField(max_length=64, null=True)
    zhongxing=models.CharField(max_length=64, null=True)
    xiaoji=models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)
    href=models.URLField(max_length=2048, null=True)

class feel_analyse3(models.Model):
    jiji=models.CharField(max_length=64, null=True)
    zhongxing=models.CharField(max_length=64, null=True)
    xiaoji=models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    share_num = models.CharField(max_length=64, null=True)
    comment_num = models.CharField(max_length=64, null=True)
    like_num = models.CharField(max_length=64, null=True)
    href=models.URLField(max_length=2048, null=True)


# --------------------------------热搜标题情感分析-------------------------------
class hot_rank_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)


class wenyu_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)


class yaowen_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)

class xiaoyuan_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)



class youxi_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)



class tiyu_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)
    href =models.TextField(max_length=2048, null=True)


#---------------------------------------热搜标题情感分析汇总-------------------------
class all_rank_analyse(models.Model):
    num_all=models.CharField(max_length=64, null=True)    #热搜数量
    jiji_add=models.CharField(max_length=64, null=True)
    zhongxing_add=models.CharField(max_length=64, null=True)
    xiaoji_add=models.CharField(max_length=64, null=True)
    zhishu_all=models.CharField(max_length=64, null=True) #情感指数



class task_list_1(models.Model):
    num = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)


