from django.shortcuts import render
# Create your views here.

def index(request):
    dict1={'text':'Hello Jaspal','number':100}
    return render(request,'basic_app/index.html',dict1)

def relative(request):
    return render(request,'basic_app/relative.html')

def other(request):
    return render(request,'basic_app/other.html')
