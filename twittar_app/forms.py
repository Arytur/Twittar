from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea

from twittar_app.models import Tweet, Comments, Message


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 60, 'rows': 4}),
        }


class SendMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['message']
        widgets = {
            'message': Textarea(attrs={'cols': 60, 'rows': 4}),
        }

