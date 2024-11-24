from advertisement.forms import CampaignForm
from advertisement.utils import convert_xml
from advertisement.models import Advertisement
from dashboard.utils import S3ImageUploader
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect


class CreateCampaign(CreateView):
    """
    Create campaign
    """
    model = Advertisement
    template_name = "advertisement/create_campaign.html"
    form_class = CampaignForm

    def get_success_url(self):
        return reverse_lazy("campaign")

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
            image = cleaned_data.pop("image")
            adv = self.model.objects.create(**cleaned_data)
            adv.save()
            s3_uploader = S3ImageUploader()
            image_url_s3 = s3_uploader.store_image(image, adv)
            adv.image_url = image_url_s3
            adv.save()
            return redirect(self.get_success_url())

        return super().form_invalid(form)


class UpdateCampaign(UpdateView):
    """
    Update campaign
    """
    model = Advertisement
    template_name = "advertisement/update_campaign.html"
    form_class = CampaignForm

    def get_success_url(self):
        return reverse_lazy("campaign")

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
            image = cleaned_data.pop("image")
            adv = self.model.objects.filter(id=self.kwargs["pk"])
            adv.update(**cleaned_data)
            adv_obj = adv[0]
            if image:
                s3_uploader = S3ImageUploader()
                image_url_s3 = s3_uploader.store_image(image, adv_obj)
                adv_obj.image_url = image_url_s3
                adv_obj.save()
            xml_data = convert_xml(adv_obj)
            adv_obj.xml_data = xml_data
            adv_obj.save()
            return redirect(self.get_success_url())

        return super().form_invalid(form)
