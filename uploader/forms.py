from django import forms

class DataFileForm(forms.Form):
    datafile = forms.FileField(label='Select a data file')

# this isn't working. I'm not sure why. I probably should keep it, but i don't know why. 
class EditDataForm(forms.Form):
    class Meta:
        fields = ['text']
        widgets = {
            'text': forms.HiddenInput(
                attrs={'id': 'edit-data', 'required': True, 'placeholder': 'no data'}
            ),
        }