from django import forms
from .models import UserProfile,Neighborhood,Business,Post,Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','bio','neighborhood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
