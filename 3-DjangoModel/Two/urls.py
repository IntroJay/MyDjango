from django.conf.urls import url

from Two import views

urlpatterns = [
    url('^index/',views.index),
    url('^home/', views.home),
    url('^addgames/', views.add_games),
    url('^getgames/', views.get_games),
    url('^taocan/', views.taocan),
    # url('^/', views.),
]