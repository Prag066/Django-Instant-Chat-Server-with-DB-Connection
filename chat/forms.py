from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser
# from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')