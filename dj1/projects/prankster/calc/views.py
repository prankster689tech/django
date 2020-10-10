from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    val="yogesh"
    return render(request, 'home.html', {'name': val})


def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2

    return render(request, "result.html", {'result': res})