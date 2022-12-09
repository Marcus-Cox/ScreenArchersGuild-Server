from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import ScreenshotCategory

class ScreenshotCategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        screenshotcategory = ScreenshotCategory.objects.get(pk=pk)
        serializer = ScreenshotCategorySerializer(screenshotcategory)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        screenshotcategory = ScreenshotCategory.objects.all()
        serializer = ScreenshotCategorySerializer(screenshotcategory, many=True)
        return Response(serializer.data)


class ScreenshotCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ScreenshotCategory
        fields = ('id', 'category','screenshot')
        depth = 2
