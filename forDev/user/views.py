from django.shortcuts import redirect, render
from .forms import UserForm
from .models import Profile
from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @csrf_exempt
    def post(self, request):
        user_id = request.POST.get("username")
        user_pw = request.POST.get("password")

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# 회원가입 Form 보여주기
def signup(request):
    form = UserForm()
    return render(request, "user/signup.html", {"form": form})


def mypage(request):
    if request.method == "POST":
        print(request.POST.get["image"])
        form = UserForm(request.POST, instance=request.user)
        form.email = request.POST["email"]
        form.profile = request.POST["profile"]
        form.image = request.FILES["image"]
        form.save()
        return redirect("board:index")
    else:
        return render(request, "user/mypage.html")
