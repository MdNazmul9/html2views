from django.urls import path
from .views import infoCreate

urlpatterns = [
    path('', infoCreate),
    
]
