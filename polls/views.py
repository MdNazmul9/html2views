from django.shortcuts import render
import json
from .models import SendingInfo
from .forms import SendingInfoForm



def infoCreate(request):

    context = {
       
    }
    return render(request, "Createinfo.html", context)
         


# from  django.views.generic import  ListView, DetailView
# from  django.views.generic.edit CreateView, UpdateView, DeleteView

# def infoCreate(request):
#     form = SendingInfoForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = SendingInfoForm()


#     context = {
#         'form': form
#     }
#     return render(request, "Createinfo.html", context)
         
