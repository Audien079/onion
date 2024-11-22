from django.db import models
from users.models import BaseModel


class Advertisement(BaseModel):
    """
    Advertisement model
    """
    title = models.CharField(max_length=300)
    xml_data = models.TextField()

    def __str__(self):
        return self.title
