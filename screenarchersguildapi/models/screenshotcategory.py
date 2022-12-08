from django.db import models
from .category import Category
from .screenshot import Screenshot
class ScreenshotCategory(models.Model):
    category_id = models.ForeignKey (Category, on_delete=models.CASCADE)
    screenshot_id = models.ForeignKey (Screenshot, on_delete=models.CASCADE)
