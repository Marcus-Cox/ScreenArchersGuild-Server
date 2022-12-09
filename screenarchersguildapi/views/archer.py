from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import Archer

class ArcherView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        archer = Archer.objects.get(pk=pk)
        serializer = ArcherSerializer(archer)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        archer = Archer.objects.all()
        serializer = ArcherSerializer(archer, many=True)
        return Response(serializer.data)


class ArcherSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Archer
        fields = ('id', 'user','bio')
        depth = 2
