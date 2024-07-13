from .models import Character, Episode
from rest_framework import serializers

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'race', 'age', 'voice_actors', 'summary']

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ['number', 'title', 'directed_by', 'written_by', 'storyboarded_by', 'original_air_date', 'summary']