# from turtle import title
# from tkinter import CASCADE
import email
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from datetime import datetime



# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=25,default='')
    first_name=models.CharField(max_length=15,default='')
    last_name=models.CharField(max_length=15,default='')
    username=models.CharField(max_length=15,default='')
    password = models.CharField(max_length=15,default='')
    confirm_password = models.CharField(max_length=15,default='')
    
        
      
    # password1=models.
# class Login(models.Model):
#     email=models.ForeignKey("User",on_delete=models.CASCADE,related_name='User_login')
    
class Profile(models.Model):
    username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='User_username')
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

class Category(models.TextChoices):
    SPORTS= 'Sports'
    ENTERTAINMENT= 'Entertainment'
    POLITICS= 'Politics' 
class Create(models.Model):
    publisher_profile_picture = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='Publisher_profile_picture')
    publisher_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Publisher_username')
    title=models.TextField(max_length=100, null=False)
    category = models.CharField(max_length=20, choices=Category.choices, default='SPORTS')
    
    cover = models.ImageField(default='default.jpg', upload_to='story_cover')
    story=models.TextField(max_length=2000, null=False)
    
    
class Story(models.Model):
     story_publisher_profile_picture = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='Story_publisher_profile_picture')
     story_publisher_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Story_publisher_username')
     publish_date=models.DateTimeField()
     story_title=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_title')
     story_cover=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_cover')
     story_update=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_Update')
     likes=models.IntegerField()
     reader_comment=models.ForeignKey("Comment",on_delete=models.CASCADE,related_name='Reader_comment')
     category_choice=models.CharField(max_length=20, choices=Category.choices, default='SPORTS')
     
    #  comments=models.ExpressionList()
     
class Comment(models.Model):
    commenter_picture = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='Commenter_profile_picture')
    commenter_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Commenter_username')
    commenting_date=models.DateTimeField()
    comment=models.TextField(max_length=1000,null=False)
    
class Like(models.Model):
    like_profile_picture = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='Like_profile_picture')
    like_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Like_username')
    

    
    
     
    
     


    
   
    


