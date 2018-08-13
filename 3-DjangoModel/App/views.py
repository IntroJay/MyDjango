import random

from django.db.models import Max, F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
from App.models import Person, People, Grade


# 首页
def index(request):
    return HttpResponse('Index')


# 批量添加人员
def add_persons(request):
    for i in range(10):
        p = Person()
        p.p_name = '啥子%d' % random.randrange(100)
        p.p_age = random.randrange(200)
        p.save()

        return HttpResponse('创建人员成功')


# 查找人员
def get_persons(request):
    # personsc= Person.objects.all()
    persons = Person.objects.filter(p_age__in=[173, 54, 3, 2])

    data = {
        "persons": persons,
    }

    return render(request, 'PersonList.html', context=data)


# 获取最大年龄的人员
def person_info(request):
    result = Person.objects.aggregate(Max("p_age"))

    print(result)

    return HttpResponse("获取最大年龄")


# 批量添加人
def add_peoples(request):
    for i in range(10):
        p = People()
        p.p_name = "又有%d" % random.randrange(100)
        p.save()

    return HttpResponse("创建people成功")


# 获取人
def get_peoples(request):
    peoples = People.objects.filter(p_register__month=9)

    data = {
        "peoples": peoples,
    }

    return render(request, 'PeopleList.html', context=data)


# 批量添加班级
def add_grades(request):
    for i in range(10):
        g = Grade()
        g.g_name = 'Python180%d' % random.randrange(10)
        g.g_boy_num = random.randrange(50)
        g.g_girl_num = random.randrange(66)
        g.save()

    return HttpResponse("创建班级成功")


# 获取班级 多种方式
def get_grades(request):
    # 获取女生比男生多的班级
    # grades = Grade.objects.filter(g_girl_num__gt=F('g_boy_num'))
    # 女生比男生加30还多的人
    # grades = Grade.objects.filter(g_girl_num__gt=F('g_boy_num')+30)
    # Q对象 支持逻辑运算     加~(取反)
    # grades = Grade.objects.filter(Q(g_girl_num__gt=F('g_boy_num') + 30))
    # Q条件查询  可一次使用多个filter
    # grades = Grade.g_objects.filter(Q(g_boy_num__gt=27) & Q(g_boy_num__lt=30))
    # 查询未删除(逻辑删除)的班级
    grades = Grade.g_objects.all().filter(is_delete=False)

    # print(len(grades))            打印班级对象的个数
    # print(Grade)                  打印这个班级类
    # print(Grade.objects)          打印班级对象
    # print(Grade.objects.all())    打印班级对象的全部
    # print(type(Grade.objects))    打印班级对象的属性

    return render(request, 'GradeList.html', context={'grades': grades})


# t通过在models中改写create_grade函数 添加班级
def add_grade(request):
    grade = Grade.g_objects.create_grade('python1888')
    grade.save()

    return HttpResponse('创建班级成功')


# 删除班级
def delete_grade(reuqest):
    grade = Grade.g_objects.last()
    grade.delete()

    return HttpResponse('删除班级成功')


# 更新班级信息
def update_grade(request):
    grade = Grade.g_objects.last()
    grade.is_delete = True
    grade.g_boy_num = 18
    grade.save()
    print(grade.g_boy_num)

    return HttpResponse('信息更新成功')
