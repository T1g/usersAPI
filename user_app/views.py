from rest_framework import permissions, viewsets
from .models import Character, Episode
from user_app.serializers import CharacterSerializer, EpisodeSerializer
    
class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('number')
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]