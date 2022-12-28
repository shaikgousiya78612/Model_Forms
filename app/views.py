from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_Topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('model is saved successfuly')
    return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    form=WebpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('insert_Webpage is successfully')
    return render(request,'insert_Webpage.html',d)



def insert_Ac(request):
    form=AccessRecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('the data is insert_Ac successfully')
        
    return render(request,'insert_Ac.html',d)