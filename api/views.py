from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from twitter.api.serializers import FollowerUpdateSerializer, \
    TwitterPostSerializer, TwitterPostListSerializer
from twitter.models import TwitterProfile, TwitterPosts, TwitterFollowers


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """

    :param request: {'username': 'shakshi', 'password': 'grubox@123'}
    :return: {"token": token} if user authenticated else 404
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class UpdateFollowerClass(CreateAPIView):
    """
    DRF Classview to create follower for a user
    :param request: {'user': 2, 'follower': 1} , where value of user and follower is twitterprofile id
    :return: success if follower is succesfully updated 
    """
    serializer_class = FollowerUpdateSerializer
    queryset = TwitterProfile.objects.all()


class PostTweetClass(CreateAPIView):
    """
    DRF Classview to create twitter posts
    :param request: {'post': "Post data", 'user': 1}
    :return: success if post is succesfullly created
    """
    serializer_class = TwitterPostSerializer
    queryset = TwitterPosts.objects.all()


class PostsListClass(ListAPIView):
    """
    DRF Classview to give list of posts posted by the people followed by request user
    """
    serializer_class = TwitterPostListSerializer

    def get_queryset(self):
        twitter_profile = TwitterProfile.objects.get(user=self.request.user)
        followers = list(TwitterFollowers.objects.filter(
            user=twitter_profile).values_list('follower', flat=True))
        posts = TwitterPosts.objects.filter(
            posted_by__in=followers).order_by('created_at')
        return posts
