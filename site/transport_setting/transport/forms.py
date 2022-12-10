from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'user_surname', 'user_number', 'rubric')
