from django.urls import path
from report.views import ReportListView, AddWebsite


urlpatterns = [
    path('websites/', ReportListView.as_view(), name='website_report'),
    path('add/website/', AddWebsite.as_view(), name='add_website'),
]
