from report.models import Website
from django import forms


class WebsiteForm(forms.ModelForm):
    """
    Add website form
    """

    class Meta:
        model = Website
        fields = [
            "web_url"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["web_url"].label = False
