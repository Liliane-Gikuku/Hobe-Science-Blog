import profile
from django.shortcuts import render

# Create your views here.
from hobeapp.models import User, Profile, Create, Story
from .forms import UserRegistrationForm, ProfileRegistrationForm, CreateRegistrationForm, StoryRegistrationForm, LikeRegistrationForm

# Create your views here.
def register_user(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm()
    return render(request,"hobeproject/register_user.html",{"form":form})


def list_user(request):
    users=User.objects.all()
    return render(request,"hobeproject/user_list.html",{"users":users})



def register_profile(request):
    if request.method=="POST":
        form=ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProfileRegistrationForm()
    return render(request,"hobeproject/register_profile.html",{"form":form})


def list_profile(request):
    profiles=Profile.objects.all()
    return render(request,"hobeproject/profile_list.html",{"profiles":profiles})


def create_story(request):
    if request.method=="POST":
        form=CreateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CreateRegistrationForm()
    return render(request,"hobeproject/create_story.html",{"form":form})


def list_draft(request):
    drafts=Create.objects.all()
    return render(request,"hobeproject/create_list.html",{"drafts":drafts})


def view_story(request):
    if request.method=="POST":
        form=StoryRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=StoryRegistrationForm()
    return render(request,"hobeproject/register_story.html",{"form":form})


def list_story(request):
    stories=Story.objects.all()
    return render(request,"hobeproject/story_list.html",{"stories":stories})




def home_page(request):
    # trending= Story.objects.count()
    # write= Create.objects.count()
    
    # profile= Profile.objects.count()
    # data={ "Trending": trending, "Write": write, "Profile":profile}
    return render(request,"hobeproject/homepage.html")