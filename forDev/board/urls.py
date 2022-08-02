from django.urls import path
from .views.base_views import IndexView

app_name = "board"

urlpatterns = [
    path("api/", IndexView.as_view()),
]
