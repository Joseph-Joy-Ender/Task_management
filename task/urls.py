from django.urls import path

from . import views

urlpatterns = [
    path("hello/", views.create_task)
]
