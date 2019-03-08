from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'BSgridapp/index.html')


def page2(request):
    return render(request, 'BSgridapp/page2.html')


def page3(request):
    return render(request, 'BSgridapp/page3.html')
