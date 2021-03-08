from django import forms
from  .models import SendingInfo

class SendingInfoForm(forms.ModelForm):
    class Meta:
        model = SendingInfo
        fields = '__all__'


class  RawSendingInfoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
