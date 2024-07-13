from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Profile, Episode
from user_app.serializers import GroupSerializer, UserSerializer, ProfileSerializer, EpisodeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET', 'POST'])
# def profile_list(request):
#     if request.method == 'GET':
#         snippets = Profile.objects.all()
#         serializer = ProfileSerializer
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('birthday')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('number')
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# from django.http import HttpResponse
# from django.template import loader
# from .models import User

# def user_app(request):
#   myusers = User.objects.all().values()
#   template = loader.get_template('all_users.html')
#   context = {
#     'myusers' : myusers,
#   }
#   return HttpResponse(template.render(context, request))

# def details(request, id):
#   myuser = User.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'myuser': myuser,
#   }
#   return HttpResponse(template.render(context, request))