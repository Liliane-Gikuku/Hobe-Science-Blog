from django.urls import path
from .views import create_story, home_page, list_draft, list_profile, list_story, register_profile, register_user, list_user, view_story
urlpatterns =[
    path("",register_user, name="registration"),
    path("users/",list_user, name="users_list"),
    path("profile/",register_profile, name="create_profile"),
    path("profiles/",list_profile, name="profiles_list"),
    path("create/",create_story, name="create_new_story"),
    path("drafts/",list_draft, name="drafts_list"),
     path("story/",view_story, name="view_story"),
    path("stories/",list_story, name="stories_list"),
    path("home/",home_page, name="home_view")
    
    
    ]
    