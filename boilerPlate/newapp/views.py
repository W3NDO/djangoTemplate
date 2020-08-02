from django.shortcuts import render
from .models import TemporaryModel
from django.views.generic import *

# Create your views here.
class HomePageView(ListView):
    model = TemporaryModel
    template_name = 'index.html'
