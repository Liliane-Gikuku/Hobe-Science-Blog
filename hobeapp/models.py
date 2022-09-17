# from turtle import title
# from tkinter import CASCADE
import email
import re
from sre_constants import CATEGORY
from turtle import title
from unicodedata import category
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=25,default='')
    first_name=models.CharField(max_length=15,default='')
    last_name=models.CharField(max_length=15,default='')
    username=models.CharField(max_length=15,default='')
    password = models.CharField(max_length=15,default='')
    confirm_password = models.CharField(max_length=15,default='')
    # user_id=models.CharField(max_length=200)
    
    

   
      
    # password1=models.
# class Login(models.Model):
#     email=models.ForeignKey("User",on_delete=models.CASCADE,related_name='User_login')
    
# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     email_confirmed = models.BooleanField(default=False)

# class Profile(models.Model):

#     NARRATESTATUS = (
#         ('PAS', 'Passed'),
#         ('REV', 'For_Review'),
#         ('ACC', 'Narration_Accepted'),
#     )

#     TRANSLATESTATUS = (
#         ('PSD', 'Passed'),
#         ('RVW', 'For_Review'),
#         ('ACP', 'Translation_Accepted'),
#     )

#     user = models.OneToOneField(User, max_length=50, related_name='userprofile',on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     narrate = models.TextField(max_length=9999, default='Enter Narration')
#     review_narration = models.CharField(max_length=50, choices=NARRATESTATUS, default='Reviewing Narration')
#     translate = models.TextField(max_length=9999, default='Enter Translation')
#     review_translation = models.CharField(max_length=50, choices=TRANSLATESTATUS, default='Reviewing Translation')

#     def __str__(self):
#         return self.user

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            img.thumbnail(output_size)
#            img.save(self.image.path)
   
    
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()



class Category(models.TextChoices):
    BIOLOGY= 'Biology'
    CHEMISTRY= 'Chemistry'
    GEOGRAPHY= 'Geography' 
    PHYSICS= 'Physics' 
    MATHS= 'Maths' 
class Create(models.Model):
    # publisher_profile_picture = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='Publisher_profile_picture')
    # publisher_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Publisher_username')
    title=models.TextField(max_length=100, default='')
    category = models.CharField(max_length=20, choices=Category.choices, default='CHEMISTRY')
    
    cover = models.ImageField(default='default.jpg', upload_to='story_cover')
    story=models.TextField(max_length=2000, null=False,default='')
    

       
class Story(models.Model):
    #  story_publisher_profile_picture = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='Story_publisher_profile_picture')
     story_publisher_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Story_publisher_username',default='')
     publish_date=models.DateTimeField()
     story_title=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_title',default='')
     story_cover=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_cover',default='')
     story_update=models.ForeignKey("Create",on_delete=models.CASCADE,related_name='Story_Update',default='')
     
     reader_comment=models.ForeignKey("Comment",on_delete=models.CASCADE,related_name='Reader_comment',default='')
     category_choice=models.CharField(max_length=20, choices=Category.choices, default='SPORTS')
     
    #  comments=models.ExpressionList()
     
class Article(models.Model):
    author=models.ForeignKey("User",on_delete=models.CASCADE,related_name="user",default='')
    headline=models.CharField(max_length=70,default='')
    description=models.TextField(max_length=500,default='')
    image=models.TextField(default='')
    category_choice=models.CharField(max_length=20, choices=Category.choices, default='SPORTS')
   
    

    
class Comment(models.Model):
    article=models.ForeignKey("Article",on_delete=models.CASCADE,related_name="comment_on_article",default='')
    # commenter_picture = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='Commenter_profile_picture')
    # commenter_username=models.ForeignKey("User",on_delete=models.CASCADE,related_name='Commenter_username')
    commenting_date=models.DateTimeField()
    comment=models.TextField(max_length=1000,default='') 
    commenter=models.CharField(max_length=50,default='')

    
    
     
    
     


    
   
    


