from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task', create_task, name='create_task'),
    path('task-status/<str:status_key>/', task_status, name='task_status'),
    path('delete-task/<str:delete_key>/', delete_task, name='delete_task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', add_task_ajax, name='add_task_ajax'),
]