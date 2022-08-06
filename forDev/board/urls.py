from django.urls import path
from .views.base_views import *
from .views import base_views

app_name = "board"

urlpatterns = [
    # Create Test Case
    # path("test/", base_views.test, name="test"),
    path("api/", IndexView.as_view()),
    path("api/<int:id>", ContentView.as_view()),
    path("", base_views.index, name="index"),
]
