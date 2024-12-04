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
            "has_image",
            "title",
            "sub_title_1",
            "sub_title_2",
            "description",
            "website",
            "company",
            "button_text",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["has_image"].label = ""
        self.fields["title"].label = False
        self.fields["sub_title_1"].label = False
        self.fields["sub_title_2"].label = False
        self.fields["description"].label = False
        self.fields["website"].label = False
        self.fields["company"].label = False
        self.fields["button_text"].label = False
        self.fields["image"].label = False
