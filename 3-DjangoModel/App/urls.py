from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addpersons/', views.add_persons),
    url(r'^getpersons/', views.get_persons),
    url(r'^addpeoples/', views.add_peoples),
    url(r'^getpeoples/', views.get_peoples),
    url(r'^personinfo/', views.person_info),
    url(r'^addgrade/', views.add_grades),
    url(r'^getgrades/', views.get_grades),
    url(r'^addgrade/', views.add_grade),
    url(r'^deletegrade/', views.delete_grade),
    url(r'^updategrade/', views.update_grade),

]
