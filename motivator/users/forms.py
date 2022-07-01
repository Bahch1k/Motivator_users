
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Motivation, User

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class MotivationForm(forms.ModelForm):


    class Meta:
        
        model = Motivation
        fields = ('motivation',)
        widgets = {
                'motivation': forms.Textarea(attrs={
            'class': 'form-control mt-4',
            'placeholder': 'Напишите свою мотивацию.'
                    }),
        }
