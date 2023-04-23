from django.shortcuts import render
from .models import Acad, Rezume

def index(reqest):
    projects = Rezume.objects.all()
    return render(reqest, 'rezume/index.html', {'projects':projects})

def acad(reqest):
    projects = Acad.objects.all()
    return render(reqest, 'rezume/acad.html', {'projects':projects})

def arbeit(reqest):

    return render(reqest, 'rezume/arbeit.html')

def programm(reqest):
    return render(reqest, 'rezume/programm.html')

