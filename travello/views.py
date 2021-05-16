from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The class'
    dest1.price = '506'
    return render(request, "index1.html",{'dest1': dest1})
