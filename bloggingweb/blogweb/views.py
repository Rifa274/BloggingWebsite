from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def print_hello(request):
    return HttpResponse("Hello world!")
def first_html(request):
    return render(request,"first.html")
