from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def abd(request):
    return HttpResponse('<h1>mr 360 in the cricket<h1>')
