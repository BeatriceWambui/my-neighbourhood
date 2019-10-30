from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Neighbourhood,My_User,Businesses,Post 


def SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','location','occupants']

class UserForm(forms.ModelForm):
        class Meta:
            model = My_User
            fields = ['username','user_id','email']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Businesses
        fields = ['business_name','business_email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','address']