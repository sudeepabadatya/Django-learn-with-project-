from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World! Welcome to my Django project's home page.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, World! Welcome to my Django project's about page.")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello, World! Welcome to my Django project's contact page.")
    return render(request, 'contact.html')

