from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# NameSpace 지정
app_name = "user"

urlpatterns = [
    # django.contrib.auth 에서 제공하는 로그인 View 클래스 호출
    # 기본 호출 경로 : registeration/login.html ==> template_name 별도 지정 필요
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "signup/",
        views.signup,
        name="signup",
    ),
]
