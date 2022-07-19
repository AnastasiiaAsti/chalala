from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Message, Profile

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phrase = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar','name','email', 'phrase']

class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields= ['text']