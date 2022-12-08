from django.db import models

class EditingTools(models.Model):
    name = models.CharField(max_length=255)