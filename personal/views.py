from django.shortcuts import render
from django.conf import settings

def home_screen_view(request, *arg, **kwargs):
    context= {}
    return render(request, "personal/home.html", context)
