from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import submittedEmails

class signUp(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(signUp, self).__init__(*args, **kwargs)

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<ul class="form-text small"> <li>Your Password should be of minimum 8 characters </li> <li> Your password must contain a number and a special character</li><li>Your password can\'t be too common</li></ul>'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<ul class="form-text small"><li>Enter the same password one more time to proceed</li> </ul>'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '<ul class="form-text small"><li> Username musn\'t contain any special characters</li></ul>'

class submitEmail(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = submittedEmails