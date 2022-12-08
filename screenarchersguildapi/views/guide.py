""" Module for Guide Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screenarchersguildapi.models import Archer
from screenarchersguildapi.models import Guide


class GuideView(ViewSet):
    """ Guide Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Guide item """
        try:
            guide = Guide.objects.get(pk=pk)
            serializer = GuideSerializer(guide)
            return Response(serializer.data)
        except Guide.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Guide items """
        guide = Guide.objects.all()
        serializer = GuideSerializer(guide, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Guide item """
        # incoming_user = request.auth.user
        writer  = Archer.objects.get(user=request.auth.user)
                
        new_guide = Guide.objects.create(
            writer=writer,
            title=request.data["title"],
            description=request.data["description"],
            content=request.data["content"],
            publishing_date=request.data["publishing_date"]
            )
        serializer = GuideSerializer(new_guide)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Guide item """
        editing_guide = Guide.objects.get(pk=pk)
        editing_guide.title = request.data["title"]
        editing_guide.description = request.data["description"]
        editing_guide.content = request.data["content"]
        editing_guide.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Guide item """
        try:
            guide = Guide.objects.get(pk=pk)
            guide.delete()
        except Guide.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GuideSerializer(serializers.ModelSerializer):
    """ JSON serializer for Guide items """
    class Meta:
        model = Guide
        fields = (
            'id',
            'writer',
            'title',
            'description',
            'content',
            'publishing_date'
            )
