import xmltodict
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Advertisement.objects.all()
        ads_json = []
        for obj in queryset:
            try:
                ad_dict = xmltodict.parse(obj.xml_data)
                ad_dict["raw_xml"] = obj.xml_data
                ad_dict["title"] = obj.title
                ads_json.append(ad_dict)
            except Exception as e:
                ads_json.append(f"Error parsing XML: {str(e)}")

        context["adds"] = ads_json
        return context
