from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import UserBase
from .forms import RegisterForm

# Create your views here.
class RegisterView(CreateView):
    model = UserBase
    form_class = RegisterForm