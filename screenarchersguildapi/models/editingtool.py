from django.db import models

class EditingTool(models.Model):
    name = models.CharField(max_length=255)