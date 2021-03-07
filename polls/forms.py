from django import forms
from  .models import SendingInfo

class SendingInfoForm(forms.ModelForm):
    class Meta:
        model = SendingInfo
        fields = '__all__'