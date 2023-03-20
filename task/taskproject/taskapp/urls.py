from django.urls import path

from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('getdata', views.getdata, name="getdata"),
    path('completed', views.completed, name="completed"),
    path('registerr', views.register, name="register"),
    path('loginn', views.login, name="login"),
    path('logout', views.logout, name="logout"),

]