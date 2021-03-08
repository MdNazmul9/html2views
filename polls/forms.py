from django import forms
from  .models import SendingInfo

class SendingInfoForm(forms.ModelForm):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={"placeholder": "Enter your title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=True, 
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows":10,
                "column":30


            }
        )
    )
    price = forms.DecimalField(initial=20.00)

    class Meta:
        model = SendingInfo
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "md" in title:
            raise forms.ValidationError("This is not valid title")

        return title

    def clean_email(self, *args, **kwargs):
        title = self.cleaned_data.get("email")
        if not "edu" in title:
            raise forms.ValidationError("This is not valid email")

        return title


    


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
