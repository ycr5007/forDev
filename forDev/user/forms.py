from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    profile = forms.CharField(label="인사말")
    image = forms.FileField()

    class Meta:
        model = User
        fields = ("username", "email")
