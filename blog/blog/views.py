from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, you meeting Aditya")
    return render(request, 'website/index.html')