from django.shortcuts import render
from django.http import HttpResponse
from calc.functions.function import handle_uploaded_file
# Create your views here.
def home(request):
    return render(request, 'index.html',{'name':'Sagar'})
def index(request):
    if request.method == 'POST':
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        return render(request,"index.html")

def alllink(request):
    pass
