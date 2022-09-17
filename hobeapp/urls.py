from django.urls import path
from . import views
from .views import create_article, create_story, home_page, list_article, list_draft, list_story, post_story, register_user, list_user, view_story,activate
from hobeapp import views as core_views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns







urlpatterns =[
    path("",register_user, name="registration"),
    path("users/",list_user, name="users_list"),
    # path("profile/",register_profile, name="create_profile"),
    # path("profiles/",list_profile, name="profiles_list"),
    path("create/",create_story, name="create_new_story"),
    path("drafts/",list_draft, name="drafts_list"),
    path("story/",view_story, name="view_story"),
    path("stories/",list_story, name="stories_list"),
    path("home/",home_page, name="home_view"),
    path("new/",post_story, name="post_view"),
    path("article/",create_article,name="create_view"),
    path("articles/",list_article, name="article_view"),
    # path("account_activation_sent/$/",activate, name="account_activation_sent"),
    # path("activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$/",activate, name="activate"),
    # url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     core_views.activate, name='activate'),

    
    
   
#    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
   path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
   path('activate/<uidb64>/<token>/', core_views.activate, name='activate'),
   


    
    
    ]
    