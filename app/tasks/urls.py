from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TaskStatsView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task_list_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('stats/', TaskStatsView.as_view(), name='task_stats'),
]
