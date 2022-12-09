from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import EditingTool

class EditingToolView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        editingTool = EditingTool.objects.get(pk=pk)
        serializer = EditingToolSerializer(editingTool)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        editingTool = EditingTool.objects.all()
        serializer = EditingToolSerializer(editingTool, many=True)
        return Response(serializer.data)


class EditingToolSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = EditingTool
        fields = ('id', 'name')
        depth = 2
