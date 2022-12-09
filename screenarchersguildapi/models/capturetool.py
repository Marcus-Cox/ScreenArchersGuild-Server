from django.db import models

class CaptureTool(models.Model):
    name = models.CharField(max_length=255)