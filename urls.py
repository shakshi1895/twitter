from django.conf.urls import url

from twitter.views import create_twitter_post

urlpatterns = [
    url(r'^create_post/$', create_twitter_post, name='create_twitter_post')
]