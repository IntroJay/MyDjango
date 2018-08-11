import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Grade, Teacher

#添加班级
def add_grade(request):
    grade = Grade()
    grade.g_name = 'python18120'
    grade.g_info = 'python'
    grade.save()
    return HttpResponse("新建一个班级")


# 生成返回语句 返回班级列表
def get_grade(request):
    grades = Grade.objects.all()

    return render(request, 'GradeList.html', context={"gradelist": grades})

#第二个应用
def hello(request):
    return HttpResponse('qwer')

#添加老师
def add_teacher(request):
    teacher = Teacher.objects.create(
        t_name='Rock%d' % random.randrange(20),
        t_age=random.randrange(18, 40))
    teacher.save()
    return HttpResponse('对象创建成功%d' % teacher.id)

#获取单个老师
def get_teacher(request):
    #  pk ------ primary key
    teacher = Teacher.objects.get(pk=1)
    # teacher = Teacher.objects.get(t_age=27)
    # teacher = Teacher.objects.first()
    # teacher = Teacher.objects.last()

    #通过教师名字查询
    teachers = Teacher.objects.filter(t_name='Rock10')
    # if teachers.exists():
    #     teacher = teachers.first()

    # if teachers.count() > 0:
    #     teacher = teachers.first()
    #     print(teacher.t_name)
    #     return HttpResponse('获取成功')
    # else:
    #     return HttpResponse('指定对象不存在')



    return HttpResponse(teacher.t_name)

#获取多个老师
def get_teachers(request):
    # teachers = Teacher.objects.filter(t_age__lt=39).filter(t_age__gt=25)

    # teachers = Teacher.objects.filter(t_name__istartswith='rock')
    teachers = Teacher.objects.filter(t_hobby__isnull='null')



    #打印对象类型
    print(type(teachers))
    print(teachers)
    #把对象以字典书形式输出
    print(teachers.values())

    data = {
        'teachers': teachers,
    }

    return render(request, 'TeacherList.html', context=data)
