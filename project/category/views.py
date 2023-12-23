from django.shortcuts import render,redirect
from . import forms
from . import models

def add_model(request): 
     Model=models.Model()
     return render(request,'model.html',{'model':Model})


def add_form(request): 
    form = forms.Form()  
    # if request.method == 'POST':
    #     form =form.Form(request.POST)    
    return render(request, 'form.html', {'form': form})
