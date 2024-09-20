from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Drop a file', widget=forms.FileInput(attrs={'accept':'application/wav'}))
