from django import forms

class DataFileForm(forms.Form):
    datafile = forms.FileField(label='Select a data file')
