from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

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
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("mypage/", views.mypage, name="mypage"),
    path("register/", RegisterView.as_view()),
    path("login_token/", LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
