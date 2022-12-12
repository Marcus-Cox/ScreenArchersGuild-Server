from django.db import models
from .category import Category
from .screenshot import Screenshot

class ScreenshotCategory(models.Model):
    category = models.ManyToManyField (Category)
    screenshot = models.ManyToManyField (Screenshot)
