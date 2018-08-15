from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='intro'),
    url(r'^userinfo/', views.user_info),
    url(r'^home/', views.home),
    url(r'^getstudents/(\d+)/', views.get_students),
    url(r'^getdate/(\d+)/(\d+)/(\d+)/', views.get_date, name='get_date'),
    url(r'^getdate2/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.get_date2,name='get_date2'),
    url(r'^mine/', views.mine),
    url(r'^getreverse/', views.get_reverse),
    # url(r'^/', views),

]
