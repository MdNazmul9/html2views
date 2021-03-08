from django import forms
from  .models import SendingInfo

class SendingInfoForm(forms.ModelForm):
    class Meta:
        model = SendingInfo
        fields = '__all__'


class  RawSendingInfoForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={"placeholder": "Enter your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows":10,
                "column":30


            }
        )
    )
    price = forms.DecimalField(initial=20.00)
