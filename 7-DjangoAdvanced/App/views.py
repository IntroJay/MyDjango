import random
from io import BytesIO
from time import sleep

from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.decorators.cache import cache_page

from App.models import Student


def index(request):
    return HttpResponse('index')


def add_students(request):
    for i in range(10):
        s = Student()
        flag = random.randrange(500)
        s.s_name = "爱上网的笑话%d" % flag
        s.s_age = random.randrange(17, 50)
        s.save()
    return HttpResponse("创建学生成功")


def get_students(request):
    students = Student.objects.all()
    # 指定页数
    page_num = int(request.GET.get("page", 1))
    # 将学生进行分页
    paginator = Paginator(students, 10)
    # 获取指定页面的学生
    page = paginator.page(page_num)

    data = {
        "students": page.object_list,
        "page_object": page,
        "page_range": paginator.page_range,
    }
    return render(request, 'StudentList.html', context=data)


# 绘制验证码
def get_verify_code(request):
    # 设置画布大小
    image_size = (200, 100)
    # 设置画布背景颜色
    image_color = get_color()
    # 生成画布
    image = Image.new("RGB", image_size, image_color)

    # 导入字体 设置字体大小
    image_font = ImageFont.truetype('/home/intro/django/day07/DjangoAdvanced/static/fonts/ADOBEARABIC-BOLD.OTF',
                                    size=60)

    # 生成画笔
    image_draw = ImageDraw.Draw(image, "RGB")

    # 字符串库
    source_str = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    dest_str = ""
    # 取四次字符
    for i in range(4):
        r = random.randrange(len(source_str))
        dest_str += source_str[r]

    # 将dest_str存到session中
    request.session['verifycode'] = dest_str

    # 起点,需要画的内容,实例化字体
    # image_draw.text((20, 30), "q", font=image_font)
    # image_draw.text((65, 30), "W", font=image_font)
    # image_draw.text((110, 30), "e", font=image_font)
    # image_draw.text((155, 30), "R", font=image_font)
    for i in range(4):
        image_draw.text((20 + 45 * i, 20), dest_str[i], fill=get_color(), font=image_font)

    # 干扰点
    for i in range(1000):
        image_draw.point((random.randrange(200), random.randrange(100)), fill=get_color())

    # 实例化一个IO流
    buffer = BytesIO()
    # 将图片存储到流中 格式是png
    image.save(buffer, "png")

    return HttpResponse(buffer.getvalue(), content_type="image/png")


# 生成随机颜色
def get_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r, g, b)


# 返回登录界面
def user_login(request):
    return render(request, 'UserLogin.html')


# 执行登录
def do_user_login(request):
    #获取用户输入的验证码
    verify_code = request.POST.get("verifycode")
    #系统生成的验证码
    dest_code = request.session.get('verifycode')

    #判断输入的验证码是否正确,并且忽略大小写
    if verify_code.lower() == dest_code.lower():
        return HttpResponse('验证成功')
    return HttpResponse("验证失败")


# 富文本(有问题)
def suggest(request):
    if request.method == "GET":
        return render(request, 'Suggest.html')
    elif request.method == "POST":
        content = request.POST.get("content")
        print(content)
        return HttpResponse("提交成功")


# 使用装饰器 缓存时间为20s
@cache_page(20)
def get_sleeping(request):
    sleep(5)
    print("学习,断片了")
    return HttpResponse("我不是故意的")


# 不使用装饰器 自己写缓存
def get_last(request):
    # 从缓存中获取缓存
    result = cache.get("get_last")
    # 如果存在直接返回
    if result:
        return HttpResponse(result)

    # 睡6s
    sleep(6)
    print("你完了")

    students = Student.objects.all()
    data = {
        "students": students,
    }
    #渲染模板 返回数据
    result = loader.get_template('StudentList.html').render(context=data)
    #保存缓存 cache.set(缓存名, 缓存数据, 缓存时长)
    cache.set(request.META.get("REMOTE_ADDR") + 'get_last', result, timeout=20)

    return HttpResponse(result)
