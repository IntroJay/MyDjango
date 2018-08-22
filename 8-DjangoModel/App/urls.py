from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^addperson/', views.add_person, name='add_person'),
    url(r'^addidcard/', views.add_idcard, name='add_idcard'),
    url(r'^deleteperson/', views.delete_person, name='delete_person'),
    url(r'^deleteidcard/', views.delete_idcard, name='delete_idcard'),

    url(r'^addgrade/', views.add_grade),
    url(r'^addstudent/', views.add_student),
    url(r'^deletestudent/', views.delete_student, name='delete_student'),
    url(r'^deletegrade/', views.delete_grade, name='delete_grade'),
    url(r'^gpbi/', views.get_person_by_idcard, name='get_person_by_idcard'),
    url(r'^gibp/', views.get_idcard_by_person, name='get_idcard_by_person'),
    url(r'^ggbs/', views.get_grade_by_student, name='get_grade_by_student'),
    url(r'^gsbg/', views.get_student_by_grade, name='get_student_by_grade'),
    url(r'^rsfg/', views.remove_student_from_grade, name='remove_student_from_grade'),
    url(r'^asfg/', views.add_student_from_grade, name='add_student_form_grade'),
    url(r'^rasfg/', views.remove_allstudent_from_grade, name='remove_allstudent_from_grade'),

    url(r'^addgoods/', views.add_goods, name='add_goods'),
    url(r'^addbuyer/', views.add_buyer, name='add_buyer'),
    url(r'^agtb/', views.add_goods_to_buyer, name='add_goods_to_buyer'),
    url(r'^bbg/', views.buyer_buy_goods, name='buyer_buy_good'),
    url(r'^gbfg/', views.get_buyers_from_goods, name='get_buyers_from_goods'),
    url(r'^ggbb/', views.get_goods_by_buyer, name='get_goods_by_buyer'),
    url(r'^deletebuyer/', views.delete_buyer, name='delete_buyer'),
    url(r'^deletegoods/', views.delete_goods, name='delete_goods'),
    # url(r'^/', views.),
    # url(r'^/', views.),
    # url(r'^/', views.),

]
