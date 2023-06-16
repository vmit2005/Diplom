from django.shortcuts import render
from .models import Acad, Rezume, Arbeit, Proggg

def index(request):
    projects = Rezume.objects.all()
    return render(request, 'rezume/index.html', {'projects':projects})

def acad(request):
    projects = Acad.objects.all()
    return render(request, 'rezume/acad.html', {'projects':projects})

def arbeit(request):
    projects = Arbeit.objects.all()
    return render(request, 'rezume/arbeit.html', {'projects':projects})

def programm(request):
    projects = Proggg.objects.all()
    return render(request, 'rezume/programm.html', {'projects':projects})

def signupuser(request):
    return render(request, 'feedback/signupuser.html' )
