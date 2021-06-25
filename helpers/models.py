from django.db import models
from django.db.models import fields



class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
