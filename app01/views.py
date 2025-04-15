from celery.concurrency import thread
from django.core.cache import cache
from django.db.models.fields import json
from django.shortcuts import render, redirect
import datetime
import uuid

from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.pagination import Pagination


import json
import websocket
import hmac
import hashlib
import base64
from urllib.parse import urlencode, urlparse
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
import ssl
import threading

# Create your views here.
# 登录页面
def login(request):
    # 定一个为空的错误接收
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 判断数据库中有没有账号密码
        ret = models.User.objects.filter(username=username, password=password)
        if ret:
            # 登录到安静博客
            return redirect('/new_layouts/')
        else:
            # 登录失败
            error_msg = '用户名或密码错误，请重新输入！'
    return render(request, 'login.html', {'error_msg': error_msg})



# 创建一个新用户
def register(request):
    # 定义一个错误提示为空
    error_name = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_list = models.User.objects.filter(username=user)
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % user
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'register.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(username=user,
                                              password=password,
                                              email=email)
            user.save()
            return redirect('/login/')
    return render(request, 'register.html')



def new_layouts(request):
    return render(request,'new_layouts.html')

def layout(request):
    return render(request,'layout.html')

def layouts(request):
    return render(request, 'layouts.html')


#系统首页
def index_2(request):
    # """ 数据统计页面 """
    huati_add_5 = models.all_rank_analyse.objects.all()

    data_list =models.hot_rank.objects.all()
    wenyu_rank_list = models.yule_rank.objects.all()
    yaowen_rank_list = models.yaowen_rank.objects.all()
    xiaoyuan_rank_list = models.xiaoyuan_rank.objects.all()
    tiyu_rank_list = models.tiyu_rank.objects.all()
    youxi_rank_list = models.youxi_rank.objects.all()
    return render(request, 'index_2.html',
                  {
                   'huati_add_5':huati_add_5,
                   'data_list':data_list,
                   'wenyu_rank_list':wenyu_rank_list,
                   'yaowen_rank_list':yaowen_rank_list,
                   'xiaoyuan_rank_list':xiaoyuan_rank_list,
                   'tiyu_rank_list':tiyu_rank_list,
                   'youxi_rank_list':youxi_rank_list})



#任务控制
def task_list(request):
    """任务列表"""
    queryset = models.task_list_1.objects.all()
    return render(request, 'task_list.html', {'queryset': queryset})

def task_add(request):
    """任务列表"""

    if request.method == "GET":
        return render(request, 'task_list.html')
    # 获取用户提交的数据
    num = request.POST.get("num")
    name = request.POST.get("name")
    time = request.POST.get("time")

    # 添加到数据库
    models.task_list_1.objects.create(num=num, name=name, time=time)

    return redirect("/task_list/")


def task_delete(request):
    # 获取ID
    # http: // 127.0.0.1: 8000 / task_delete /?nid = 1
    nid = request.GET.get('nid')
    # 删除
    models.task_list_1.objects.filter(id=nid).delete()

    # 重定向回任务列表
    return redirect("/task_list/")


#情感分析
def analyse(request):
    huati_add_5 = models.all_rank_analyse.objects.all()

    return render(request, 'analyse.html',
                  { 'huati_add_5': huati_add_5})


def analyse_2(request):
    hot_1 = models.hot_rank_result.objects.all()  # 热搜
    hot_2 = models.wenyu_result.objects.all()  # 文娱
    hot_3 = models.yaowen_result.objects.all()  # 要闻
    hot_4 = models.xiaoyuan_result.objects.all()  # 校园
    hot_5 = models.youxi_result.objects.all()  # 游戏
    hot_6 = models.tiyu_result.objects.all()    #体育

    return render(request, 'analyse_2.html',
                  {'hot_1': hot_1,'hot_2': hot_2,
                   'hot_3': hot_3, 'hot_4': hot_4,'hot_5': hot_5,'hot_6': hot_6})

def project_detail(request):
    return render(request, 'project_detail.html')


def trace(request):
    data_list =models.hot_rank.objects.all()
    data_1 = models.feel_analyse.objects.filter(key_s="积极").order_by('-like_num')  # 315
    data_2 = models.feel_analyse3.objects.filter(key_s="积极").order_by('-like_num')  # 哪吒2
    data_3 = models.feel_analyse2.objects.filter(key_s="积极").order_by('-like_num')  # deepseek
    # 三个重点话题的相关话题
    data_4 = models.feel_analyse.objects.filter(key_s="消极").order_by('-like_num')
    data_5 = models.feel_analyse3.objects.filter(key_s="消极").order_by('-like_num')
    data_6 = models.feel_analyse2.objects.filter(key_s="消极").order_by('-like_num')

    huati_add_3 = models.all_rank_analyse.objects.all()

    return render(request, 'trace.html',
                  {'data_list': data_list,
                   'data_1': data_1,
                   "data_2": data_2,
                   "data_3": data_3,
                   "data_4": data_4,
                   "data_5": data_5,
                   "data_6": data_6
                   }
                  )



def trace_2(request):
    data_list_0 = models.all_rank_analyse.objects.all()
    data_list_1 = models.feel_analyse.objects.all()  # 315晚会
    data_list_2 = models.feel_analyse3.objects.all()  # 哪吒2
    data_list_3 = models.feel_analyse2.objects.all()  # deepseek

    return render(request, 'trace_2.html',
                  {'data_list_0': data_list_0, 'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3})



# ------------------------------------星火api-----------------------------------
class Ws_Param(object):
    # 保持原有Ws_Param类不变
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    def create_url(self):
        # 保持原有create_url方法不变
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        signature_origin = f"host: {self.host}\ndate: {date}\nGET {self.path} HTTP/1.1"
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        v = {"authorization": authorization, "date": date, "host": self.host}
        return self.gpt_url + '?' + urlencode(v)


def on_message(ws, message, task_id):
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]

        # 结构化处理
        structured_content = content.replace("1.", "\n1.").replace("2.", "\n2.")
        keywords = ['事件背景', '发展过程', '社会影响', '舆论特征', '后续预测']

        current_data = cache.get(task_id) or {'content': '', 'status': 'processing', 'complete': False}
        for kw in keywords:
            if kw in structured_content:
                structured_content = structured_content.replace(kw, f'【{kw}】')

        current_data['content'] += structured_content

        if status == 2:
            current_data['complete'] = True
            current_data['status'] = 'done'
            ws.close()

        cache.set(task_id, current_data, timeout=300)


def on_error(ws, error):
    print("### error:", error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    ws.send(json.dumps(ws.params))


def gen_params(appid, query, domain):
    system_prompt = """作为微博热搜分析师，请按以下结构分析：
1. 事件背景（200字，说明起源）
2. 发展过程（按时间线分3-5个阶段）
3. 关键参与方（当事人、机构、媒体等）
4. 社会影响（分短期/长期，需数据支持）
5. 舆论特征（情感分析、观点分布）
6. 后续预测（3种可能发展路径）
使用专业但易懂的语言，标注数据来源，保持客观中立。"""

    return {
        "header": {"app_id": appid, "uid": str(uuid.uuid4())},
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.3,
                "max_tokens": 4096,
                "auditing": "default",
            }
        },
        "payload": {
            "message": {
                "text": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"分析以下微博热搜事件：{query}"}
                ]
            }
        }
    }


@csrf_exempt
def get_gpt_answer(request):
    appid = "29eab5a3"
    api_secret = "MzVmMzM3YmIxM2EwYzhlOGViY2I0NDBm"
    api_key = "930ee9d56e7e87f0601731e3e813191a"
    gpt_url = "wss://spark-api.xf-yun.com/v3.5/chat"
    domain = "generalv3.5"

    if request.method == "POST":
        query = request.POST.get('query')
        if not query:
            return JsonResponse({"status": "error", "message": "请输入分析内容"})

        task_id = str(uuid.uuid4())
        cache.set(task_id, {
            'status': 'processing',
            'content': '分析启动...\n',
            'complete': False
        }, 300)

        threading.Thread(
            target=start_ws_connection,
            args=(appid, api_secret, api_key, gpt_url, domain, query, task_id)
        ).start()

        return JsonResponse({"status": "processing", "task_id": task_id})

    return render(request, 'chat.html')


@csrf_exempt
def get_answer(request):
    task_id = request.GET.get('task_id')
    if not task_id:
        return JsonResponse({"status": "error", "message": "参数错误"})

    data = cache.get(task_id) or {}
    return JsonResponse({
        "status": data.get('status', 'error'),
        "content": data.get('content', '分析结果不可用'),
        "complete": data.get('complete', True)
    })


def start_ws_connection(appid, api_secret, api_key, gpt_url, domain, query, task_id):
    ws_param = Ws_Param(appid, api_key, api_secret, gpt_url)
    ws_url = ws_param.create_url()

    ws = websocket.WebSocketApp(
        ws_url,
        on_message=lambda ws, msg: on_message(ws, msg, task_id),
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.params = gen_params(appid, query, domain)
    ws.run_forever()