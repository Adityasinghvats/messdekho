from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # it takes tuples as it it inbuilt
        fields = ('username', 'email', 'password1', 'password2')
        
# class TweetSearchForm(forms.Form):
#     tweet = forms.ModelChoiceField(queryset=Tweet.objects.all(),empty_label="Select Tweet")
class TweetSearchForm(forms.Form):
    tweet = forms.CharField(label="Search", required=True)