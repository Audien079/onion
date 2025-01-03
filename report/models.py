from django.db import models
from users.models import BaseModel
from report.enums import WebType


class Website(BaseModel):
    """Websites model"""
    web_url = models.URLField(max_length=400)
    status = models.BooleanField(default=False)
    last_check = models.DateTimeField(null=True, blank=True)
    last_active = models.DateTimeField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    type = models.CharField(
        max_length=30, choices=WebType.choices(), null=True, blank=True
    )

    def __str__(self):
        return self.web_url
