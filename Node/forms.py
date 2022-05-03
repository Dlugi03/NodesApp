from django import forms

class AddNodeForm(forms.Form):
    name = forms.CharField(label="New Node", max_length=30)