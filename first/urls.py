"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.conf.urls.static import static
from app01 import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/',views.login),

    path('register/', views.register),

    path('layout/',views.layout),


    path('new_layouts/',views.new_layouts),


    # 超话管理
    path('layouts/',views.layouts),


    path('index_2/', views.index_2),


    #任务控制
    path('task_list/', views.task_list),


    #情感分析
    path('analyse/', views.analyse),
    path('analyse_2/', views.analyse_2),

    path('trace/', views.trace),
    path('trace_2/', views.trace_2),

    path('get_gpt_answer/', views.get_gpt_answer, name='get_gpt_answer'),
    path('get_answer/', views.get_answer, name='get_answer'),  # 新增这行

]



