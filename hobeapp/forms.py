from django import forms
# from django.contrib.auth.forms import UserRegistrationForm, ProfileRegistrationForm,CreateRegistrationForm,StoryRegistrationForm,CommentRegistrationForm,LikeRegistrationForm
from .models import Article, User, Create, Story, Comment

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    email = forms.EmailField(max_length=254, help_text='')
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    
    


    class Meta:
          model=User
          fields="__all__"
        #   fields = ('first_name', 'last_name', 'email','username','password', 'confirm_password')
        
# class ProfileRegistrationForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields="__all__"
    
    
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
        

class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model=Article
        fields="__all__"

        
