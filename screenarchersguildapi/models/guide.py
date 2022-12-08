from django.db import models
from .archer import Archer

class Guide(models.Model):
    writer = models.ForeignKey(Archer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)