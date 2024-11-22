from rest_framework import serializers
from advertisement.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """
    Advertisement serializer
    """

    class Meta:
        model = Advertisement
        fields = ["id", "title", "xml_data"]