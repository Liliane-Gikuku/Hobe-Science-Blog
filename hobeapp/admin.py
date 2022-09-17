from django.contrib import admin

# Register your models here.
from .models import Article, User,Create,Story,Comment
# , Profile,Create,Story,Comment
class UserAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name")
    searchFields=("first_name", "last_name")
admin.site.register(User,UserAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display=("author", "headline","description","image")
    searchFields=("author", "headline")
admin.site.register(Article,ArticleAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display=("user","image")
#     searchFields=("user","image")
# admin.site.register(Profile,ProfileAdmin)

class CreateAdmin(admin.ModelAdmin):
    list_display=("title","cover")
    searchFields=("title","cover")
admin.site.register(Create,CreateAdmin)

class StoryAdmin(admin.ModelAdmin):
    list_display=("story_title","story_cover")
    searchFields=("story_title","story_cover")
admin.site.register(Story,StoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=("article","commenter","commenting_date","comment")
    searchFields=("commenting_date","comment")
admin.site.register(Comment,CommentAdmin)



