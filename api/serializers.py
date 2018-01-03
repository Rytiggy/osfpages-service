from .models import Home
from rest_framework import serializers


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    unpublished_page_data = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    class Meta:
        model = Home
        fields = ('guid', 'page_data', 'unpublished_page_data', 'meta_data')
