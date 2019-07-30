from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('ID', 'PW', 'name', 'studentNum', 'major', 'gender', 'email', 'isHantor',)
