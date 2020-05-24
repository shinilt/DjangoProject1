from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Sayhello(request):
    #return HttpResponse('<h1>This is from the django DemoApp</h1>')
    return render(request,'DemoApp/Sayhello.html')
