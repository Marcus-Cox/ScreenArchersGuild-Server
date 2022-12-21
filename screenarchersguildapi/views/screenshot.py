""" Module for Screenshot Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import Archer,Screenshot,CaptureTool,EditingTool,Category
 
class ScreenshotView(ViewSet):
    """ Screenshot Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Screenshot item """
        try:
            screenshot = Screenshot.objects.get(pk=pk)
            serializer = ScreenshotSerializer(screenshot)
            return Response(serializer.data)
        except Screenshot.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Screenshot items """
        screenshot = Screenshot.objects.all()
        serializer = ScreenshotSerializer(screenshot, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Screenshot item """
        # incoming_user = request.auth.user
        archer  = Archer.objects.get(user=request.auth.user)
        captureTool = CaptureTool.objects.get(pk=request.data["captureTool"])
        editingTool = EditingTool.objects.get(pk=request.data["editingTool"])
        category = Category.objects.get(pk=request.data["category"])
        
        new_screenshot = Screenshot.objects.create(
            archer=archer,
            image=request.data["image"],
            content=request.data["content"],
            captureTool=captureTool,
            editingTool=editingTool,
            category = category,
            timestamp=request.data["timestamp"]
            )
        serializer = ScreenshotSerializer(new_screenshot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Screenshot item """
        
        captureTool = CaptureTool.objects.get(pk=request.data["captureTool"])
        editingTool = EditingTool.objects.get(pk=request.data["editingTool"])
        category = Category.objects.get(pk=request.data["category"])

        editing_screenshot = Screenshot.objects.get(pk=pk)
        editing_screenshot.image = request.data["image"]
        editing_screenshot.content = request.data["content"]
        editing_screenshot.captureTool = captureTool
        editing_screenshot.editingTool = editingTool
        editing_screenshot.category =category
        editing_screenshot.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Screenshot item """
        try:
            screenshot = Screenshot.objects.get(pk=pk)
            screenshot.delete()
        except Screenshot.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ScreenshotCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('description',)

class ScreenshotSerializer(serializers.ModelSerializer):
    """ JSON serializer for Screenshot items """
    class Meta:
        model = Screenshot
        fields = (
            'id',
            'archer',
            'image',
            'content',
            'captureTool',
            'editingTool',
            'category',
            'timestamp'
            )
