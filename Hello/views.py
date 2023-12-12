from django.shortcuts import render
from django.http import HttpResponse  #import HttpResponse, after installing app in settings
# Create your views here.
from django import forms
from .forms import studentform
from .models import students

form = studentform()
my_dict = { "insert_me": "Its lowest...","sr":"Star dust", "Army": "Purple you","n":300,"form":form}
def index(request):  #2.1 create a function index with parameter request
    return HttpResponse("<h1> I started learning Django and its fun </h1>") #2.3 to respond

def Hello(request):
    # return HttpResponse("<h2> I am coming from the application urls.py file </h2>")
    if request.method =='POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentform()
    return render(request,'Hello/Home.html', context=my_dict)
def hi(request):
    return HttpResponse("<h3> HIII </h3>")

def list_view(request):

    #dictionary for initial data with
    #field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = students.objects.all()
    return render(request, "Hello/list_view.html", context)
