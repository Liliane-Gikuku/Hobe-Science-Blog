import profile
from django.shortcuts import render
from django.views import generic


# Create your views here.
from hobeapp.models import User, Create, Story
from .forms import UserRegistrationForm,CreateRegistrationForm, StoryRegistrationForm, ArticleRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import loader
# from .tokens import account_activation_token

# Create your views here.
def register_user(request):
    
    # if request is not post, initialize an empty form
    form=UserRegistrationForm(request.POST or None)
    if request.method=="POST":
        
    
     if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = UserRegistrationForm()
    return render(request, "hobeproject/register_user.html", {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
    


def list_user(request):
    users=User.objects.all()
    return render(request,"hobeproject/user_list.html",{"users":users})



# def register_profile(request):
#     if request.method=="POST":
#         form=ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=ProfileRegistrationForm()
#     return render(request,"hobeproject/register_profile.html",{"form":form})


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

def create_article(request):
    if request.method=="POST":
        form=ArticleRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ArticleRegistrationForm()
    return render(request,"hobeproject/create_article.html",{"form":form})


def list_article(request):
    articles=Create.objects.all()
    return render(request,"hobeproject/article_list.html",{"articles":articles})
    


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

def account_activation_sent(request):
    
    return render(request,"hobeproject/register_user.html")






    
def post_story(request):
    if request.method=="POST":
        form=PostRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PostRegistrationForm()
    return render(request,"hobeproject/post.html",{"form":form})

# http://127.0.0.1:8000/api/v1/articles