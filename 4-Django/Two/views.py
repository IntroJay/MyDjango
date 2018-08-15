import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Grade, Student


# index
def index(request):
    return HttpResponse('index')


# 添加班级
def add_grade(request):
    g = Grade()
    g.s_name = 'python1806%d' % random.randrange(100)
    g.save()

    return HttpResponse('创建班级成功%d' % g.id)


# 添加学生
def add_student(request):
    s = Student()
    s.s_name = 'intro%d' % random.randrange(200)
    s.s_age = random.randrange(17, 36)

    g = Grade.objects.last()
    s.s_grade = g
    s.save()

    return HttpResponse('创建学生成功%d' % s.id)


# 获取班级
def get_grades(request):
    grades = Grade.objects.all()

    return render(request, 'GradeList.html', context={"grades": grades})


# 先获取班级id,再获取某个班级的学生
def get_students(request, gradeid):
    students = Student.objects.filter(s_grade=gradeid)

    return render(request, 'StudentList.html', context={"students": students})


# request请求
def send_request(request):
    print(type(request))  # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.path)  # /two/sendrequest/
    print(request.method)  # GET
    print(request.encoding)  # None
    print(request.GET)  # <QueryDict: {}>
    print(request.POST)  # <QueryDict: {}>
    # print(request.META)   # 一堆信息

    print(request.GET.getlist("user"))  # 获取url中传递的多个user

    # meta = request.META
    # keys = meta.keys()
    # for key in keys:
    #     print(key, meta.get(key))
    #     print("****************")

    # print(meta.get('REMOTE_ADDR'))
    # if meta.get("REMOTE_ADDR") =="10.0.118.33":
    #     return HttpResponse('请求失败了')
    # print(meta.get('USER'))

    return HttpResponse('请求成功')


# 获取用户账号密码
def send_post(request):
    return render(request, 'SendPost.html')
