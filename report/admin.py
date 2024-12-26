from django.contrib import admin
from report.models import Website


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    """
    Website data view in admin panel
    """

    list_display = ["web_url", "id", "status", "type"]
    search_fields = ["web_url"]
