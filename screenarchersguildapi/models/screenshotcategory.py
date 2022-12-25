from django.db import models
from .screenshot import Screenshot

class ScreenshotCategory(models.Model):
    screenshot = models.ForeignKey (Screenshot, on_delete=models.CASCADE)
    category = models.ForeignKey ('Category', on_delete=models.CASCADE, related_name="screenshot_category")