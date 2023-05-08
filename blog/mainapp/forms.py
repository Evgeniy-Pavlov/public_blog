from django.contrib.auth.forms import UserCreationForm
from .models import UserBase
from django import forms


class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('usertag', 'email', 'password1', 'password2', 'is_company', 'company', 'logo')
