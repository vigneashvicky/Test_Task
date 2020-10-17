from django.conf.urls import url
from django.urls import path
from Test_Task.task_app import views


urlpatterns = [
    path('', views.loginIndex, name='login'),
    path('main_page/', views.main_page),
    path('submit_fun/', views.submit_fun, name='files'),
    path('filesmryget/', views.filesummary, name='filesmrydata'),
    path('loginpswd/', views.loginpswd, name='loginpswd'),



]
