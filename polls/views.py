from django.shortcuts import render
import json
from .models import SendingInfo
from .forms import SendingInfoForm, RawSendingInfoForm




def infoCreate(request):
    my_form = RawSendingInfoForm()
    if request.method == "POST":
        my_form = RawSendingInfoForm(request.POST)
        print(my_form.cleaned_data)
        SendingInfo.objects.create(**my_form.cleaned_data)
    else:
        print(my_form.errors)

    context = {
        "form": my_form
    }
    return render(request, "Createinfo.html", context)
         



# def infoCreate(request):
#     #print(request.GET)
#     # print(request.POST["email"])
#     if request.method=="POST":
#         x = request.POST.get('email')
#         print(x)
#         # Person.objects.create(email=x)

#     context = {
       
#     }
#     return render(request, "Createinfo.html", context)
         


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
         
