from django import forms

class DataFileForm(forms.Form):
    datafile = forms.FileField(label='Select a data file')

class EditDataForm(forms.Form):
    class Meta:
        fields = ['text']
        widgets = {
            'text': forms.HiddenInput(
                attrs={'id': 'edit-data', 'required': True, 'placeholder': 'no data'}
            ),
        }