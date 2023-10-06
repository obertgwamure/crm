from django import forms

class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    age = forms.IntegerField(min_value=18)
