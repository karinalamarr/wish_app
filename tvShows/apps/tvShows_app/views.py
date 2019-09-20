from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

def index(request):
    
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'tvShows_app/index.html', context)


def new(request):
    
    return render(request, 'tvShows_app/new_show.html')


def create(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    else:
    
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], releaseDate=request.POST['release'], description=request.POST['desc'])

        return redirect(f'/shows/{new_show.id}')


def about(request, show_id):
    
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, 'tvShows_app/about.html', context)


def edit(request, show_id):
    
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, f'tvShows_app/edit.html', context)


def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Show.objects.get(id = show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.releaseDate = request.POST['release']
        show.description = request.POST['desc']
        show.save()

        return redirect(f'/shows/{show.id}')


def destroy(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/shows')