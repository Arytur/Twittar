from django.shortcuts import render, redirect
from django.views import View
from .models import Tweet
from .forms import *
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class MainPageView(View):

    def get(self, request):
        tweets = Tweet.objects.all().order_by('-creation_date')
        return render(request, 'main.html', {'tweets': tweets})


class AddPostView(View):

    def get(self, request):
        form = AddPostForm()
        return render(request, 'add_post.html', {'form': form})

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('/')


class MyPostsView(View):

    def get(self, request):
        user = request.user
        posts = Tweet.objects.filter(user=user)
        return render(request, 'my_posts.html', {'posts': posts})













