from django.shortcuts import render, redirect
from .models import Destination


# Create your views here.




def index(request):

    # this is done without use of database

    # dest1 = Destination()
    # dest1.name = "Kathmandu"
    # dest1.desc = "The city that has temples more than houses."
    # dest1.price = 700
    # dest1.image = 'ktm.jpg'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Pokhara"
    # dest2.desc = "The city with lakes and Mountains."
    # dest2.price = 650
    # dest2.image = 'pok.jpg'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Rara"
    # dest3.desc = "The city that has hidden unexplored beauty."
    # dest3.price = 700
    # dest3.image = 'rara.jpg'
    # dest3.offer = True

    # dest = [dest1, dest2, dest3]
    
    # # return render(request, 'index.html', {'ktm': dest1, 'pok': dest2, 'rara': dest3})

    # Using Database Style
    dest = Destination.objects.all()
    return render(request, "index.html", {'dests': dest})