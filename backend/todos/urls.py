from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    # api/
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]
