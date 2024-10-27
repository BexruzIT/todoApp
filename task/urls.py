from django.urls import path
from task import views

urlpatterns = [
    path('', views.to_do, name='index'),
    path('tasks/', views.to_do_get, name='tasks'),
    path('task-receiver/', views.receiver_reminder, name='task-receiver'),
    path('task-search/', views.task_search, name="task_search")
]
