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


class MainPageView(View):

    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'main.html', {'tweets': tweets})








