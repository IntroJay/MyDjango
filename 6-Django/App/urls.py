from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^usercenter/', views.user_center, name='user_center'),
    url(r'^userregister/', views.user_register, name='user_register'),
    url(r'^userlogin/', views.user_login, name='user_login'),
    url(r'^userlogout/', views.user_logout, name='user_logout'),
    url(r'^userinfo/', views.user_info, name='user_info'),
    url(r'^getphone/', views.get_phone, name='get_phone'),
    url(r'^getticket/', views.get_ticket, name='get_ticket'),
    url(r'^getnews/', views.get_news, name='get_news'),
    url(r'^search/', views.search, name='search'),
    url(r'^makebug/', views.make_bug, name='make_bug'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^getinfo/', views.get_info, name='get_info'),
]
