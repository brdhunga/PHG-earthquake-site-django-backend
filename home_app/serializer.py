from rest_framework import serializers


class HomeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    why_us = serializers.CharField(required=True, max_length=2000)


