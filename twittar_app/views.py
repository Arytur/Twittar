from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .models import *
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


class MainPageView(LoginRequiredMixin, View):

    def get(self, request):
        tweets = Tweet.objects.all()
        ctx = {
            'tweets': tweets,
        }
        return render(request, 'main.html', ctx)


class AddPostView(LoginRequiredMixin, View):

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


class MyPostsView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        posts = Tweet.objects.filter(user=user)
        return render(request, 'my_posts.html', {'posts': posts})


class PostView(LoginRequiredMixin, View):

    def get(self, request, post_id):
        tweet = Tweet.objects.get(id=post_id)
        form = AddCommentForm()
        comments = Comments.objects.filter(tweet_id=post_id).order_by('creation_date')
        ctx = {
            'tweet': tweet,
            'form': form,
            'comments': comments
        }
        return render(request, 'post.html', ctx)

    def post(self, request, post_id):
        form = AddCommentForm(request.POST)
        tweet = Tweet.objects.get(id=post_id)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.tweet = tweet
            new_comment.save()
            return HttpResponseRedirect(self.request.path_info)


class UserInfoView(LoginRequiredMixin, View):

    def get(self, request, user_id):
        user_info = User.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user_id=user_id)
        comments = Comments.objects.filter(user_id=user_id)
        form = SendMessageForm()
        ctx = {
            'user_info': user_info,
            'tweets': tweets,
            'comments': comments,
            'form': form,
        }
        return render(request, 'user_info.html', ctx)

    def post(self, request, user_id):
        # form to send a message
        user_info = User.objects.get(id=user_id)
        form = SendMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sent_to = user_info
            new_message.sent_by = request.user
            new_message.save()
            return HttpResponseRedirect(self.request.path_info)


class MailboxView(LoginRequiredMixin, View):

    def get(self, request, user_id):
        messages = Message.objects.filter(sent_to=user_id)
        return render(request, 'mailbox.html', {'messages': messages})


class MessageView(LoginRequiredMixin, View):

    def get(self, request, user_id, mess_id):
        message = Message.objects.get(id=mess_id)
        message.read = True
        message.save()
        form = SendMessageForm()
        return render(request, 'message.html', {'message': message, 'form': form})

    def post(self, request, user_id, mess_id):
        # form to send a message
        message = Message.objects.get(id=mess_id)
        user_info = message.sent_by
        form = SendMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sent_to = user_info
            new_message.sent_by = request.user
            new_message.save()
            return HttpResponseRedirect(self.request.path_info)

