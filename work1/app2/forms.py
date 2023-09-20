from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from app2.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone')