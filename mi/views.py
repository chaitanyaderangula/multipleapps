from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def bumrha(request):
    return HttpResponse('<h1>booom boom bhumraha<h1>')
