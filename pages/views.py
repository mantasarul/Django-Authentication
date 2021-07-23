from django.shortcuts import render
from django.views.generic.base import TemplateView, View

# Create your views here.

class Home(TemplateView):
    template_name = 'pages/home.html'
