from django import forms

from twitter.models import TwitterPosts


class TwitterPostForm(forms.ModelForm):

    class Meta:
        model = TwitterPosts
        fields = ['post']