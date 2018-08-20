from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^index2/', views.index2),
    url(r'^redirect/', views.redirect_request, name='redirect_request'),
    url(r'^home/', views.home),
    url(r'^login/', views.login,name='login'),
    url(r'^dologin/', views.do_login, name='do_login'),
    url(r'^loginout/', views.loginout,name='loginout'),

    url(r'^usercenter/', views.user_center,name='user_center'),
    url(r'^userregister/', views.user_register,name='user_register'),
    url(r'^userlogin/', views.user_login,name='user_login'),
    url(r'^userlogout/', views.user_logout,name='user_logout'),
    url(r'^userinfo/', views.user_info,name='user_info'),
    # url(r'^/', views.),
    # url(r'^/', views.),

]
