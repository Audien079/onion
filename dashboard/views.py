from datetime import datetime
from users.models import User
from advertisement.models import Advertisement
from django.views.generic import TemplateView, ListView


class HomeView(TemplateView):
    """
    Clients page
    """
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CampaignView(ListView):
    """
    Campaign view to list all the advertisements
    """
    template_name = "dashboard/campaign.html"
    model = Advertisement
    queryset = Advertisement.objects.all().order_by("id")
    context_object_name = "adds"
