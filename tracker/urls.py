from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.topics_list, name='topics_list'),
    path('topics/add/', views.add_topic, name='add_topic'),
    path('topics/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    path('topics/<int:topic_id>/', views.topic_problems, name='topic_problems'),
    path('problems/<int:problem_id>/edit/', views.edit_problem, name='edit_problem'),
    path('revision/', views.revision_list, name='revision_list'),
    path('logic/', views.logic_list, name='logic_list'),
    path('', views.dashboard, name='dashboard'),
]