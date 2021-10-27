from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField(
        max_length=255,
    )
  

