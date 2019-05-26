# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.encoding import smart_str


class TwitterProfile(models.Model):
    """
    Class to store user profile
    """
    user = models.OneToOneField(User, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    user_image = models.ImageField(
        upload_to='user_images/', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(
            self.first_name,  smart_str(self.email))


class TwitterFollowers(models.Model):
    user = models.ForeignKey('TwitterProfile', related_name='User')
    follower = models.ForeignKey('TwitterProfile', related_name='Follower')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "follower"))


class TwitterPosts(models.Model):
    posted_by = models.ForeignKey('TwitterProfile',
                                  related_name='post_posted_by')
    post = models.TextField()
    liked_by = models.ManyToManyField('TwitterProfile',
                                      related_name='post_liked_by')
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)