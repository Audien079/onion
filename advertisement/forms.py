from advertisement.models import Advertisement
from django import forms


class CampaignForm(forms.ModelForm):
    """
    Campaign form to create podcast
    """
    image = forms.ImageField(required=False)

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "description",
            "website",
            "company",
            "button_text",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = False
        self.fields["description"].label = False
        self.fields["website"].label = False
        self.fields["company"].label = False
        self.fields["button_text"].label = False
        self.fields["image"].label = False