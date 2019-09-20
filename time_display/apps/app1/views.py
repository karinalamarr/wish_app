from django.shortcuts import render, HttpResponse, redirect
from time import  strftime


def index(request):
    context = {
        "date": strftime("%b %d  %Y "),
        "time": strftime(" %H : %M %p")
    }
    print(context)
    return render(request,'app1/index.html', context)
