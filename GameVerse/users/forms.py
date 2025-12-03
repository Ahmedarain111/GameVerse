from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter Email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control custom-input',
            'placeholder': 'Enter Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control custom-input',
            'placeholder': 'Confirm Password',
        })

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'Placeholder': 'Enter Username',
        'class': 'form-control custom-input'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'Placeholder': 'Enter Password',
        'class': 'form-control custom-input'
    }))
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            
            if user is None:
                raise forms.ValidationError("Invalid username or password")
            
        return cleaned_data