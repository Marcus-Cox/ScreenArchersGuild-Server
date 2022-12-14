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
        # screenshot = Screenshot.objects.all()

        # --//new branch code
        if "myScreenshots" in request.query_params:
            user = Archer.objects.get(user=request.auth.user)
            screenshot = Screenshot.objects.all().order_by('timestamp').filter(archer=user)
        else:
            screenshot = Screenshot.objects.all().order_by('timestamp')
        # --//new branch code

        serializer = ScreenshotSerializer(screenshot, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Screenshot item """
        
        archer  = Archer.objects.get(user=request.auth.user)
        captureTool = CaptureTool.objects.get(pk=request.data["captureTool"])
        editingTool = EditingTool.objects.get(pk=request.data["editingTool"])
        
        # //new code
        category = Category.objects.get(pk=request.data["category"])
        # //new code

        new_screenshot = Screenshot.objects.create(
            archer=archer,
            image=request.data["image"],
            content=request.data["content"],
            captureTool=captureTool,
            editingTool=editingTool,
            timestamp=request.data["timestamp"]
            )
        
        # //new code 1
        new_screenshot.category.set([category])  # pass a list containing the Category object
        # //new code 1
        
        #//new code 2
        # new_screenshot.category.add(category)  # use the add() method to add a single object
        #//new code 2
        
        serializer = ScreenshotSerializer(new_screenshot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Screenshot item """
        
        captureTool = CaptureTool.objects.get(pk=request.data["captureTool"])
        editingTool = EditingTool.objects.get(pk=request.data["editingTool"])
        
        # //new code
        category = Category.objects.get(pk=request.data["category"])
        # //new code
        
        editing_screenshot = Screenshot.objects.get(pk=pk)
        editing_screenshot.image = request.data["image"]
        editing_screenshot.content = request.data["content"]
        editing_screenshot.captureTool = captureTool
        editing_screenshot.editingTool = editingTool
        
        # //new code
        editing_screenshot.category.set([category])
        # //new code
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

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('description')


class CaptureToolSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaptureTool
        fields = ('name')

        
class ArcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archer
        fields = ('id', 'user','bio')
        depth = 1

class ScreenshotSerializer(serializers.ModelSerializer):
    """ JSON serializer for Screenshot items """
    archer=ArcherSerializer()
    captureTool=CaptureToolSerializer
    category=CategorySerializer
    
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

