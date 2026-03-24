from django.urls import path,include
from . import views

urlpatterns = [
    path("tasks",views.TaskView.as_view()),
    path("tasks/<int:pk>",views.SingleTaskView.as_view()),
    path("users/<int:pk>",views.UserTaskView.as_view()),
]