from django.db import models
from users.models import BaseModel


class Advertisement(BaseModel):
    """
    Advertisement model
    """
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
