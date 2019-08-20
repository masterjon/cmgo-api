from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListAPIView
# from django.db.models import Count

from . import serializers, models


class SlideViewSet(ModelViewSet):
    queryset = models.Slide.objects.all()
    serializer_class = serializers.SlideSerializer