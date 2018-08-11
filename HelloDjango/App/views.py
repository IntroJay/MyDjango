from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse('Django')


def index(request):
    return HttpResponse('<h1>Intro</h1>')


def weather(request):
    return render(request, 'weather.html')


# 在终端上显示
def get_student(request):
    students = Student.objects.all()

    for student in students:
        print(student.s_name + '是' + str(student.s_age))

    return HttpResponse('查询完毕')


# 通过模板在网页中显示
def get_student2(request):
    students = Student.objects.all()

    for student in students:
        print(student.s_name + '是' + str(student.s_age))

    return render(request, 'StudentList.html', context={'students': students})
