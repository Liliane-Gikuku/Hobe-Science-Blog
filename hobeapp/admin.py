from django.contrib import admin

# Register your models here.
from .models import User,Profile,Create,Story,Comment,Like
# , Profile,Create,Story,Comment
class UserAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name")
    searchFields=("first_name", "last_name")
admin.site.register(User,UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=("username","profile_picture")
    searchFields=("username","profile_picture")
admin.site.register(Profile,ProfileAdmin)

class CreateAdmin(admin.ModelAdmin):
    list_display=("title","cover")
    searchFields=("title","cover")
admin.site.register(Create,CreateAdmin)

class StoryAdmin(admin.ModelAdmin):
    list_display=("story_title","story_cover")
    searchFields=("story_title","story_cover")
admin.site.register(Story,StoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=("commenter_picture","commenter_username","commenting_date","comment")
    searchFields=("commenter_picture","commenter_username","commenting_date","comment")
admin.site.register(Comment,CommentAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display=("like_profile_picture","like_username")
    searchFields=("like_profile_picture","like_username")
admin.site.register(Like,LikeAdmin)

