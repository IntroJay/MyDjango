import os
import random
import time
import uuid

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import UserModel, BuyerModel


# from ..DjangDay06 import settings

# index
def index(request):
    return HttpResponse('index')


# 用户中心
def user_center(request):
    token = request.COOKIES.get('token')
    if not token:
        return render(request, 'UserCenter.html')
    try:
        user = UserModel.objects.get(u_token=token)
        username = user.u_name
        return render(request, 'UserCenter.html', context={"username": username})
    except Exception as e:
        return HttpResponse('你已被强制下线')


# 用户注册
def user_register(request):
    if request.method == 'GET':
        return render(request, 'UserRegister.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = UserModel()
        user.u_name = username
        user.u_password = password
        token = str(uuid.uuid4())
        user.u_token = token
        user.save()

        return HttpResponse('注册成功')


# 用户登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'UserLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            uuser = UserModel.objects.get(u_name=username)
            puser = UserModel.objects.get(u_password=password)
            token1 = uuser.u_token
            token2 = puser.u_token

            if token1 == token2:
                # 每次登录重新生成token  实现单终端登录
                token = str(uuid.uuid4())
                uuser.u_token = token
                uuser.save()

                response = HttpResponse('登陆成功')
                response.set_cookie('token', token1)
                return response
        except Exception as e:
            return redirect("app:user_login")


# 用户信息
# def user_info(request):
#     return None
#
# 用户退出
# def user_logout(request):
#     return None


# 中间件 抢购手机
def get_phone(request):
    if random.randrange(100) > 90:
        return HttpResponse("恭喜你抢到小米8 256G")
    return HttpResponse('正在排队')


# 中间件 抢购优惠券
def get_ticket(request):
    if random.randrange(100) > 80:
        return HttpResponse("恭喜您抢到199-188优惠券")
    return HttpResponse('下手慢了没有了')


# 获取要搜索的信息
def get_news(request):
    # 向缓存中获取缓存
    result = cache.get("get_news")
    # 如果其存在,则直接返回
    if result:
        return HttpResponse(result)
    else:
        time.sleep(3)
        result = '我发现一个同学睡着了'
        # timeout 缓存时长
        cache.set('get_news', result, timeout=15)
        return HttpResponse(result)


# 中间件 获取要搜索的内容
def search(request):
    if request.method == "GET":
        return render(request, 'Search.html')
    elif request.method == "POST":
        a = request.POST.get("context")
        return HttpResponse('一下是关于%s的网页' % a)


# 制造一个bug 当bug发生时调用中间件process_exception
def make_bug(request):
    if random.randrange(10) > 5:
        i = 1 / 0
    return HttpResponse('你是谁')


# 上传文件   (未完成)
def upload(request):
    if request.method == "GET":
        return render(request, 'Upload.html')
    elif request.method == "POST":
        # print(request.FILES)
        # icon = request.FILES.get("icon")
        #
        # save_file_path = os.path.join(settings.BASE_DIR, 'static/upload/' + str(icon))
        # with open(save_file_path, 'wb') as save_file:
        #     for part in icon.chunks:
        #         save_file.write(part)
        #         save_file.flush()
        #
        # return HttpResponse('上传成功')

        username = request.POST.get("username")
        icon = request.FILES.get('icon')
        buyer = BuyerModel()
        buyer.b_name = username
        buyer.b_icon = icon
        buyer.save()

        return HttpResponse('上传成功')


def get_info(request):
    buyer = BuyerModel.objects.last()

    data = {
        "username": buyer.b_name,
        "icon": "/static/upload" + buyer.b_icon.url
    }

    return render(request, 'Userinfo.html', context=data)
