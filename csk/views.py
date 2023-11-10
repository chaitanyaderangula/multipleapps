from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1>one and only batsman to reach the 5000 runs in ipl histiry<h1>')