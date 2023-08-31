from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('hello/helloworld',views.hello_world),
    path('',views.home_page),
    path('url/task',views.task_page)
]