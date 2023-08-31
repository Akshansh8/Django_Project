from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

def home_page(request):
    return render(request,'index.html')

def task_page(request):
    data={
        'title':'Task Page',
        'slist':['Bread','Cheese','Butter','Milk','Egg','Mayo','Flakes','Ketchup','Apple','Jam']
    }
    return render(request,"task.html",data)
    
