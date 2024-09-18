from django import forms

class File_form(forms.Form):
    file = forms.CharField(label='fileUpload')