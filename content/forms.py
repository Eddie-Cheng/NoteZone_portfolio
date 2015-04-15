from django import forms

class DetailForm(forms.Form):
    sentence = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':40})
                               , required=False)
    https = forms.URLField(required=False)
    anyfile = forms.FileField(required=False)
