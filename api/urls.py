from django.urls import path
from api.views import AddsApiView


urlpatterns = [
    path("advertisements/", AddsApiView.as_view(), name="advertisements"),
]
