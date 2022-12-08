from django.db import models

class CaptureTools(models.Model):
    name = models.CharField(max_length=255)