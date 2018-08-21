from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^addstudents/', views.add_students, name='add_students'),
    url(r'^getstudents/', views.get_students, name='get_students'),
    url(r'^getverifycode/', views.get_verify_code, name='get_verify_code'),
    url(r'^userlogin/', views.user_login, name='user_login'),
    url(r'^douserlogin/', views.do_user_login, name='do_user_login'),
    url(r'^suggest/', views.suggest, name='suggest'),
    url(r'^getsleeping/', views.get_sleeping, name='getsleeping'),
    url(r'^getlast/', views.get_last, name='get_last'),
    # url(r'^/', views., name=),

]
