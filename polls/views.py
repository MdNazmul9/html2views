from django.shortcuts import render
import json


# from  django.views.generic import  ListView, DetailView
# from  django.views.generic.edit CreateView, UpdateView, DeleteView

def infoCreate(request):
    if request.method=="POST":
        print(request.POST.get("contact_name"))

    return render(request, 'home.html')
