from uuid import uuid4
from django.db import models
from users.models import BaseModel


class Advertisement(BaseModel):
    """
    Advertisement model
    """
    add_id = models.UUIDField(
        unique=True, default=uuid4, editable=False, db_index=True
    )
    title = models.CharField(max_length=300)
    image_url = models.URLField(max_length=400, null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    button_text = models.CharField(max_length=50, null=True, blank=True)
    xml_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
