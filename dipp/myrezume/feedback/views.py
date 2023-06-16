from django.shortcuts import render
from .models import Feedback


def feedbacks(request):
    feeds=Feedback.objects.order_by('-date')
    return render(request, 'feedback/feedback.html', {'feeds':feeds})

def detail(request, feed_id):
    return render(request,'feedback/details.html',{'id':feed_id})