from rest_framework import serializers
from api.models import ShortURL


class URLSerializer(serializers.ModelSerializer):

    original_url = serializers.URLField(required=True)

    class Meta:
        model = ShortURL
        fields = ('original_url', )


class ListURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('original_url', 'short_url', 'visit_count')




