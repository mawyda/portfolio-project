# urls.py 
# 10.05.18
# for blog app - blog\\urls.py

from django.urls import path

from . import views 

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
] 
