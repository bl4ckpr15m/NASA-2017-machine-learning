from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.crypto import get_random_string

from ai.models import Picture
from nasa.serializers import PictureSerializer
from nasa import tasks as tk


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get(self, request):
        queryset = self.queryset.order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        picture = Picture()
        f = request.data['feature']
        file_name = "{}.jpg".format(get_random_string(length=10))
        picture.feature.save(file_name, f, save=True)

        # tk.PredictTask.delay(picture.pk)

        picture.label = ""
        picture.score = 0
        picture.co2 = 0.0

        picture.save()
        serializer = self.get_serializer(picture, many=False)
        return Response(serializer.data)
