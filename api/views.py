from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from advertisement.models import Advertisement
from api.serializers import AdvertisementSerializer
from api.pagination import DefaultPagination
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


class AddsApiView(ListAPIView):
    """
    Adds list view
    """
    search_fields = ["title"]
    filter_backends = [SearchFilter]
    serializer_class = AdvertisementSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Advertisement.objects.all()
        return queryset

    @method_decorator(cache_page(60 * 60))
    def get(self, *args, **kwargs):
        return super().list(*args, **kwargs)
