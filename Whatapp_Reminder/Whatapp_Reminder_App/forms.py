from .models import UserDetails
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name','email','password','phone','company_name','company_type','address']