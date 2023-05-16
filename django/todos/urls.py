from django.urls import path

from . import views


urlpatterns = [
    path('', views.CreateTodoView.as_view(), name='create-todo'),
    path('todos/<int:pk>/delete/', views.DeleteTodoView.as_view(), name='delete-todo'),
    path('todos/<int:pk>/complete/', views.CompleteTodoView.as_view(), name='complete-todo'),
]
