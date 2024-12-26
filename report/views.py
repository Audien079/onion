from report.models import Website
from report.forms import WebsiteForm
from django.views.generic import ListView, CreateView
from django.urls.base import reverse_lazy


class DomainsListView(ListView):
    """
    View to list all the Websites
    """
    template_name = "reports/domains.html"
    model = Website

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_filter = self.request.GET.get('type', None)
        if type_filter:
            context["webs"] = Website.objects.filter(type=type_filter).order_by("web_url")
        else:
            context["webs"] = Website.objects.all().order_by("web_url")
        context['selected_type'] = type_filter
        return context


class AddWebsite(CreateView):
    """
    Add Website
    """
    model = Website
    template_name = "reports/add_website.html"
    form_class = WebsiteForm

    def get_success_url(self):
        return reverse_lazy("website_report")
