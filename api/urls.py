from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    re_path('upload/(.+)/$', views.download, name='download'),
]
