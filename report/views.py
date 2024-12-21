from report.models import Website
from report.forms import WebsiteForm
from django.views.generic import TemplateView, ListView, CreateView
from django.urls.base import reverse_lazy


class ReportListView(ListView):
    """
    View to list all the Websites
    """
    template_name = "reports/websites.html"
    model = Website

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["webs"] = Website.objects.all()
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
