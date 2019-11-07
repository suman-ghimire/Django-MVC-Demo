from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    

    # text = """<h1> Welcome to my first app on Django. </h1>
    #         <p> By Suman Ghimire </p>"""
    # return HttpResponse(text)

    # new way
    return render(request, 'home.html', {'name':'Suman'})


def add(request):
    val1= request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html' ,{'result':res})
       
