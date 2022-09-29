from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Note
from django.urls import  reverse
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def index(request):
    data = Note.objects.all().order_by('date_added').values()

    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({'data': data}, request))


def add(request):
    template = loader.get_template('addNote.html')
    
    return HttpResponse(template.render({}, request))


def create(request):
    title = request.POST['title']
    content = request.POST['content']
    date_added = request.POST['date_added']
    new_note = Note(title=title, content=content, date_added=date_added)
    new_note.save()

    return redirect(reverse('index'))

def delete(request, id):
    single_note = Note.objects.get(id=id)
    single_note.delete()

    return redirect(reverse('index'))

def edit(request, id):
    edit_note = Note.objects.get(id=id)
    template = loader.get_template('editNote.html')

    return HttpResponse(template.render({'edited': edit_note}, request))

def editedNote(request, id):
    updated_note = Note.objects.all().get(id=id)
    new_title = request.POST['title']
    new_content = request.POST['content']
    new_date = request.POST['date_added']
    updated_note.title = new_title
    updated_note.content = new_content
    updated_note.date_added = new_date
    updated_note.save()

    return redirect(reverse('index'))

def deleteEditedNote(request, id):
    deleted_note = Note.objects.all().get(id=id)
    deleted_note.delete()

    return redirect(reverse('index'))