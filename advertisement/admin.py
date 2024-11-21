from django.contrib import admin
from advertisement.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """
    Advertisement data view in admin panel
    """

    list_display = ["id", "text"]
    search_fields = ["text"]

