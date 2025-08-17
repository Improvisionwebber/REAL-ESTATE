from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django import forms
from .forms import PostForm
from .models import ContactSubmission
from . forms import ContactForm
from django.contrib.auth.decorators import login_required
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
      
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
def home(request): 
    return render(request, 'home.html')
def manage(request): 
    return render(request, 'manage.html')
def about(request):
    return render(request, 'about.html')
def contact(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ContactForm()
        else:
            contactsubmission = ContactSubmission.objects.get(pk=id)
            form = ContactForm(instance=contactsubmission)
        return render(request, "contact.html", {'form':form})
    else:
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contactsubmission = ContactSubmission.objects.get(pk=id)
            form = ContactForm(request.POST, instance=contactsubmission)
        if form.is_valid():
            form.save()
        return redirect('/')
    
def contact_delete(request,id):
    dashboard = ContactSubmission.objects.get(pk=id)
    dashboard.delete()
    return redirect('/tables')
def services(request):
    posts = Post.objects.all()
    return render(request, 'services.html', {'posts':posts})
def single(request, pk):
    post = Post.objects.get(pk=pk)
    recent_posts = Post.objects.exclude(pk=pk).order_by('-id')[:3]  # last 3 excluding current
    return render(request, 'singlepage.html', {
        'post': post,
        'recent_posts': recent_posts
    })
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "register.html", {'form': form})

import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post  # make sure your Post model has an image_url field

IMGBB_API_KEY = "c346e6e29bbc0340846deb957f6d510a"

@login_required(login_url='login')
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # Upload to imgbb if an image was uploaded
            if request.FILES.get("image"):  # make sure field name is 'image'
                image_file = request.FILES["image"]

                upload_url = "https://api.imgbb.com/1/upload"
                response = requests.post(
                    upload_url,
                    data={"key": IMGBB_API_KEY},
                    files={"image": image_file.read()}
                )

                if response.status_code == 200:
                    data = response.json()
                    post.image_url = data["data"]["url"]  # save imgbb image link
                else:
                    print("Error uploading to imgbb:", response.text)
                    post.image_url = None  # fallback

            post.save()
            return redirect("services")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})


def contact(request):
    success = False  # flag to show success message

    if request.method == "POST":
        # get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # save to database only if all fields are filled
        if name and email and phone and message:
            ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            success = True  # to show success message

    return render(request, "contact.html", {"success": success})
@login_required(login_url='login')
def tables(request):
    tables = ContactSubmission.objects.all() 
    return render(request, "tables.html", {'tables': tables})
def user(request):
    return redirect('login')