from django.urls import path
from .views.base_views import IndexView
from .views import base_views

app_name = "board"

urlpatterns = [
    path("api/", IndexView.as_view()),
    path("", base_views.index, name="index"),
]
