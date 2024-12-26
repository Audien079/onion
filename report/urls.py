from django.urls import path
from report.views import DomainsListView, AddWebsite


urlpatterns = [
    path('domains/', DomainsListView.as_view(), name='domains'),
    path('add/website/', AddWebsite.as_view(), name='add_website'),
]
