from rest_framework import serializers

from ai.models import Picture


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('pk', 'feature', 'label', 'score', 'co2', 'recyclable', 'created_at')
