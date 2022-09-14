from django import forms
from .models import User, Profile, Create, Story, Comment, Like

class UserRegistrationForm(forms.ModelForm):
    class Meta:
          model=User
          fields="__all__"
        
class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"
    
    
class CreateRegistrationForm(forms.ModelForm):
    class Meta:
        model=Create
        fields="__all__"
        
class StoryRegistrationForm(forms.ModelForm):
    class Meta:
        model=Story
        fields="__all__"
        
class CommentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields="__all__"
        
class LikeRegistrationForm(forms.ModelForm):
    class Meta:
        model=Like
        fields="__all__"