from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login_app/index.html')

def success(request):
    all_users = User.objects.all()
    for user in all_users:
        print(user.first_name)
    return render(request, 'login_app/success.html')

def register(request):
    if request.method == 'POST' :
        
        errors = User.objects.basic_validator(request.POST)
        if len(errors)> 0:
            for key, values in errors.items():
                messages.error(request, value)
            return redirect ('/')
        new_user = User.objects.create(first_name=request.POST['name'], password=request.POST['password'])
        request. session['user']= new_user.first_name
        new_user.save()
        
        return redirect( '/success')
    else:
        return redirect ('/')


def login(request):
    if request.method == 'POST':
        logged_user = User.object.filter(first_name=request.POST['name'])
        if (logged_user):
                    if (logged_user[0].password == request.POST['password']):
                        request. session['user']= logged_user[0].name
                    return redirect('/success')
        else:
                return redirect('/')

