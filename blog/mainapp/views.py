from django.shortcuts import render
from django.views.generic import CreateView
from .models import UserBase

# Create your views here.
class RegisterView(CreateView):
    model = UserBase
    fields = '__all__'