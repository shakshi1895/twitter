from django.conf.urls import url

from twitter.api.views import login, UpdateFollowerClass, PostTweetClass, \
    PostsListClass

urlpatterns = [
    url(r'^login/', login),
    url(r'^UpdateFollower/$', UpdateFollowerClass.as_view()),
    url(r'^PostTweet/$', PostTweetClass.as_view()),
    url(r'^PostsList/$', PostsListClass.as_view()),
]