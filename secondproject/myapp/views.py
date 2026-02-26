from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Greet(request):
    return HttpResponse("hello world !")

def template(request):
    return render(request,'index.html')