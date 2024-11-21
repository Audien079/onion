from django.urls import path
from dashboard.views import HomeView, CampaignView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('campaign/', CampaignView.as_view(), name='campaign'),
]
