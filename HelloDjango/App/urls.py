from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^addteacher/', views.add_teacher),
    url(r'^getteacher/',views.get_teacher),
    url(r'^getteachers/',views.get_teachers),

]
