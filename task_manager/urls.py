from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('incomplete_task/<int:task_id>/', views.incomplete_task, name='incomplete_task'),
]
