import hashlib
import random
import time
from datetime import timedelta

import timed as timed
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 返回文本的方法1
from django.urls import reverse

# index  返回文本的方法1
from App.models import UserModel


def index(request):
    response = HttpResponse()
    response.content = '哈哈哈还可以这样'
    return response


# index2 返回文本的方法2
def index2(request):
    response = HttpResponse()
    response.write("这是一个马桶")
    response.flush()
    return response


def redirect_request(request):
    return redirect(reverse('app:index'))


# 主页
def home(request):
    # 获取user存入cookie
    username = request.COOKIES.get("user")

    # 设置获取user存入session
    # username = request.session.get("user")
    return render(request, 'home.html', context={"username": username})


# 登录界面
def login(request):
    return render(request, 'login.html')


# 执行登录  登录成功界面
def do_login(request):
    username = request.POST.get("username")

    response = HttpResponse('%s 登陆成功' % username)

    # max_age默认为0    max_age=None  则永远不过期
    response.set_cookie("user", username, max_age=30)

    # expires=timedelta(days=11)   Django中expires默认为14天
    # response.set_cookie("user", username, expires=timedelta(days=14))

    # 设置保存session
    # request.session['user'] = username
    return response


# 执行退出  退出成果界面
def loginout(request):
    response = HttpResponse('退出成功')
    # 删除cookie
    response.delete_cookie('user')

    # 删除sessionid  但是数据库里仍然存在其session数据  会造成垃圾
    # response.delete_cookie("sessionid")

    # 直接删除session  虽然数据库里session数据改变 但仍然存在  会造成垃圾
    # del request.session['user']

    # 全部删除session
    # request.session.flush()
    return response


# ---------------------User--------------------------


def user_center(request):
    token = request.COOKIES.get('token')
    if not token:
        return render(request, 'UserCenter.html')
    try:
        user = UserModel.objects.get(u_token=token)
        return render(request, 'UserCenter.html', context={'username': user.u_name})
    except Exception as e:
        return render(request, 'UserCenter.html')


def user_register(request):
    if request.method == "GET":
        return render(request, 'UserRegister.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel()
        user.u_name = username
        user.u_password = password

        token = generate_token(request.META.get("REMOTE_ADDR"), username)
        user.u_token = token

        user.save()

        response = HttpResponse('注册成功')
        response.set_cookie('token', token)
        return response


"""
    token需要保证唯一
    找几个唯一的数据拼接一下
    时间, ip, 随机数, username
    md5
        
"""


def generate_token(ip, username):
    t = time.time()
    r = random.random()
    before = str(t) + str(r) + str(ip) + str(username)

    md5 = hashlib.md5()
    md5.update(before.encode("utf-8"))

    return md5.hexdigest()


def user_login(request):
    return None


def user_logout(request):
    return None


def user_info(request):
    return None
