from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from .models import UserBase
from django import forms


class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    usertag = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('username', 'usertag', 'email', 'password1', 'password2', 'is_company', 'company', 'logo')


class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    usertag = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    about_me = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('username', 'usertag', 'email', 'about_me', 'is_company', 'company', 'logo')


class UpdatePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserBase
        fields = ('old_password', 'password1', 'password2')