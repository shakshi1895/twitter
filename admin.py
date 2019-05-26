# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from twitter.models import TwitterProfile, TwitterPosts, TwitterFollowers


@admin.register(TwitterProfile)
class TwitterProfileAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        "first_name", "gender", "email")


@admin.register(TwitterPosts)
class TwitterPostAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        "posted_by", "post")


@admin.register(TwitterFollowers)
class TwitterFollowerAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        "user", "follower")