from django.db import models
from .archer import Archer
from .editingtool import EditingTool
from .capturetool import CaptureTool

class Screenshot(models.Model):
    archer = models.ForeignKey (Archer, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True)
    content = models.TextField()
    captureTool = models.ForeignKey (CaptureTool, on_delete=models.CASCADE)
    editingTool = models.ForeignKey (EditingTool, on_delete=models.CASCADE)
    isMooded = models.BooleanField() 
    timestamp = models.DateField(auto_now_add=True)