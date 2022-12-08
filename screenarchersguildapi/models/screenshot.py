from django.db import models
from .archer import Archer
from .editingtools import EditingTools
from .capturetools import CaptureTools

class Screenshot(models.Model):
    archer = models.ForeignKey (Archer, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True)
    content = models.TextField()
    captureTools = models.ForeignKey (CaptureTools, on_delete=models.CASCADE)
    editingTools = models.ForeignKey (EditingTools, on_delete=models.CASCADE)
    isMooded = models.BooleanField() 
    timestamp = models.DateField(auto_now_add=True)