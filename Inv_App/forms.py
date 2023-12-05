from Inv_App.models import Message
from django import forms

class YourForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
