from django.contrib import admin
from advertisement.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """
    Advertisement data view in admin panel
    """

    list_display = ["add_id", "id", "title"]
    search_fields = ["title"]
