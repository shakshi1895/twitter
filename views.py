# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render

from twitter.forms import TwitterPostForm

# Create your views here.
from twitter.models import TwitterProfile


def create_twitter_post(request):
    """
    
    :param request: request contains twitter post data to be udpated
    :return: render twitterpost form template
    """
    if request.method == "POST":
        form = TwitterPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            twitter_profile = TwitterProfile.objects.get(user=request.user)
            post.posted_by = twitter_profile
            post.save()
            return render(request, 'twitterpostform.html',{'form': form})
        else:
            messages.success(request,
                             'There seems to be some error in form, Check Below !!')
            return render(request, 'twitterpostform.html', {'form': form})
    else:
        form = TwitterPostForm()
        return render(request, 'twitterpostform.html', {'form': form})
