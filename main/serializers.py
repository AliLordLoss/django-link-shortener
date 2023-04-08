from rest_framework import serializers
from .models import LinkMap

class LinkMapSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)
    times_followed = serializers.IntegerField(read_only=True)

    class Meta:
        model = LinkMap
        fields = '__all__'