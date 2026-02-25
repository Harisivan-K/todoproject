
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks'),
    path('toggle/<int:task_id>/', views.task_toggle, name='task_toggle'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]



