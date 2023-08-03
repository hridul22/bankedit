from django import forms
from django.contrib.auth.models import User

from .models import UserInfo,Reginfo

class NewPageForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address',]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
        }


# bank_app/forms.py




class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

