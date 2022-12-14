from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import CaptureTool

class CaptureToolView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        captureTool = CaptureTool.objects.get(pk=pk)
        serializer = CaptureToolSerializer(captureTool)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        captureTool = CaptureTool.objects.all()
        serializer = CaptureToolSerializer(captureTool, many=True)
        return Response(serializer.data)


class CaptureToolSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CaptureTool
        fields = ('id', 'name')
        depth = 2
