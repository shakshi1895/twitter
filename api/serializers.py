from rest_framework import serializers

from twitter.models import TwitterFollowers, TwitterPosts, TwitterProfile


class TwitterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterProfile
        fields = ['first_name', 'gender', 'email']


class FollowerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwitterFollowers
        fields = ['follower', 'user']


class TwitterPostListSerializer(serializers.ModelSerializer):
    posted_by = TwitterUserSerializer()

    class Meta:
        model = TwitterPosts
        fields = ['posted_by', 'post']


class TwitterPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwitterPosts
        fields = ['posted_by', 'post']