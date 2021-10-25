from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = forms.BooleanField(default=True)
    is_admin = forms.BooleanField(default=False)

