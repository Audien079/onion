from django.urls import path
from advertisement.views import CreateCampaign, UpdateCampaign


urlpatterns = [
    path("create/campaign/", CreateCampaign.as_view(), name="create_campaign"),
    path("update/<int:pk>/campaign/", UpdateCampaign.as_view(), name="update_campaign"),
]
