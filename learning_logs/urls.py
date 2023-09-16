"""
定义learnings_logs的URL模式
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
