from django import forms

class AddNodeForm(forms.Form):
    name = forms.CharField(label="New Node", max_length=30)
    
class EditNodeForm(forms.Form):
    new_name = forms.CharField(label="New Name", max_length=30)