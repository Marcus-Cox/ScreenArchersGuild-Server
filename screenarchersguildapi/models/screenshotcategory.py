from django.db import models
from .category import Category
from .screenshot import Screenshot

class ScreenshotCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField (Category)
    screenshot = models.ManyToManyField (Screenshot)
