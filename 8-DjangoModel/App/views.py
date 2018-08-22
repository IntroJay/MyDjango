import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person, IDCard, Grade, Student, Buyer, Goods

#index
def index(request):
    return HttpResponse('index')


# 添加人
def add_person(request):
    person = Person()
    person.p_name = '小明%d' % random.randrange(1000)

    person.save()
    return HttpResponse('用户创建成功%d' % person.id)


# 添加身份证
def add_idcard(request):
    idcard = IDCard()
    idcard.id_num = "10%d" % random.randrange(10000000, 99999999)

    person = Person.objects.last()
    # 声明外键关联
    idcard.id_person = person

    idcard.save()
    return HttpResponse('身份证创建成功%d' % idcard.id)


# 当被关联的数据表被删除时,关联的表数据会被级联删除
# 删除人
def delete_person(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse("成功删除用户")


# 当关联的表数据被删除时,被关联的表数据不会受影响
# 删除身份证
def delete_idcard(request):
    idcard = IDCard.objects.last()
    idcard.delete()
    return HttpResponse("成功删除身份证")


# 通过从表获取主表,要通过显性属性查找
def get_person_by_idcard(request):
    idcard = IDCard.objects.last()
    person = idcard.id_person
    print(type(person))
    return HttpResponse(person.p_name)


# 通过主表获取从表,通过隐形属性(关联表的小写模型名)获得
def get_idcard_by_person(request):
    # 方法一
    # person = Person.objects.last()
    # # person = Person()
    # idcard = person.idcard

    # 方法二
    idcard = IDCard.objects.get(id_person_id=5)

    print(type(idcard))
    return HttpResponse(idcard.id_num)


# 添加班级
def add_grade(request):
    grade = Grade()
    grade.g_name = "python18%d" % random.randrange(10, 100)

    grade.save()
    return HttpResponse('创建班级成功%d' % grade.id)


# 添加学生
def add_student(request):
    student = Student()
    student.s_name = "小小%d" % random.randrange(100)

    grade = Grade.objects.last()
    student.s_grade = grade

    student.save()
    return HttpResponse('创建学生成功%d' % student.id)


# 删除学生
def delete_student(request):
    student = Student.objects.last()
    student.delete()

    return HttpResponse('学生删除成功')


# 删除班级
def delete_grade(request):
    grade = Grade.objects.last()
    grade.delete()

    return HttpResponse('班级删除成功%')


# 通过多获取一,要通过显性属性获得
def get_grade_by_student(request):
    student = Student.objects.last()

    grade = student.s_grade
    print(type(grade))

    return HttpResponse(grade.g_name)


# 通过一获取多,要通过隐形属性获得,格式为:对象.级联数据_set    级联数据是小写模型名
def get_student_by_grade(request):
    grade = Grade.objects.last()
    # grade = Grade()

    # student = grade.student_set
    # print(type(student))

    # 获取该班级所有学生
    # students = grade.student_set.all()
    # 获取该班级名字末尾为5的学生,将结果倒序
    students = grade.student_set.filter(s_name__endswith='5').order_by('-id')

    data = {
        'students': students,
    }
    return render(request, 'StudentList.html', context=data)


# 把指定学生从班级中移除
def remove_student_from_grade(request):
    grade = Grade.objects.last()

    student = Student.objects.get(pk=70)

    grade.student_set.remove(student)

    return HttpResponse("移除成功")


# 把指定学生添加到班级中
def add_student_from_grade(request):
    grade = Grade.objects.last()

    student = Student.objects.get(pk=70)

    grade.student_set.add(student)

    return HttpResponse('大神已进班')


# 把该班级的所有学生移除
def remove_allstudent_from_grade(request):
    grade = Grade.objects.last()

    grade.student_set.clear()

    return HttpResponse("该班级学生已清空")


# 添加买手
def add_buyer(request):
    buyer = Buyer()
    buyer.b_name = '剁手者%d' % random.randrange(50)

    buyer.save()
    return HttpResponse('创建剁手这成功%d' % buyer.id)


# 添加商品
def add_goods(request):
    goods = Goods()
    goods.g_name = "拯救者%d" % random.randrange(2000)

    goods.save()
    return HttpResponse('商品添加成功%d' % goods.id)


# 往从表添加数据 添加商品并给买手
def add_goods_to_buyer(request):
    goods = Goods.objects.last()
    buyer = Buyer.objects.last()

    goods.g_buyer.add(buyer)
    # print(goods.g_buyer)
    print(type(goods.g_buyer))
    return HttpResponse('剁手成功')


# 往主表添加数据 通过隐形属性
def buyer_buy_goods(request):
    buyer = Buyer.objects.last()
    goods = Goods.objects.last()

    # buyer = Buyer()
    buyer.goods_set.add(goods)
    return HttpResponse('购买成功')


# 获取商该品的所有卖家,并展示
def get_buyers_from_goods(request):
    goods = Goods.objects.last()
    buyers = goods.g_buyer.all()

    data = {
        "buyers": buyers,
    }
    return render(request, 'BuyerList.html', context=data)


# 获取该买手买的所有商品
def get_goods_by_buyer(request):
    buyer = Buyer.objects.last()
    goods = Goods.objects.all()

    goods_list = buyer.goods_set.all()

    data = {
        "goods_list": goods_list,
    }
    return render(request, 'GoodsList.html', context=data)


# 删除买手
def delete_buyer(request):
    buyer = Buyer.objects.last()
    buyer.delete()
    return HttpResponse('删除一个剁手者')


# 删除商品
def delete_goods(request):
    goods = Goods.objects.last()
    goods.delete()
    return HttpResponse('删除商品')
