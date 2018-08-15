import random

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

#加载渲染index2.html
def index(request):
    return render(request, 'index2.html')

#返回Json数据
def user_info(request):
    data = {
        "name": 'Tom',
        "age": "18",
        "hobby": 'eat,sleep',
    }
    return JsonResponse(data)


# 重定向
def home(request):
    # if random.randrange(100) > 95:
    #     return HttpResponseRedirect('/app/index/')
    # else:
    #     return HttpResponse('欢迎回来')
    # return HttpResponseRedirect('/app/index')
    return HttpResponseRedirect(reverse('python:intro'))


# 通过url传递参数
def get_students(request, gradeid):
    print(gradeid)
    print(type(gradeid))
    return HttpResponse('获取%s班的学生' % gradeid)


# 通过url获得日期 多个参数按照参数进行匹配
def get_date(request, year, month, day):
    return HttpResponse("%s年%s月%s日" % (year, month, day))


# 通过url获得日期 (?<year>\d+)
def get_date2(request, month, year, day):
    return HttpResponse("%s年%s月%s日" % (year, month, day))


def mine(request):
    return render(request, 'mine.html')

#url反向解析在views中的使用
def get_reverse(request):
    result = reverse("python:get_date", args=(2018, 11, 11))
    print(result)

    result1 = reverse("python:get_date2", kwargs={"year": 2018, "month": 6, "day": 18})
    print(result1)

    return HttpResponseRedirect(result)
