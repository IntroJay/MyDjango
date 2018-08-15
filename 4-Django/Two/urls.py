from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addgrade/', views.add_grade),
    url(r'^addstudent/', views.add_student),
    url(r'^getgrades/', views.get_grades),
    url(r'^getstudents/(?P<gradeid>\d+)/', views.get_students, name='get_students'),
    url(r'^sendrequest/', views.send_request, name='send_request'),
    url(r'^sendpost/', views.send_post),

]
