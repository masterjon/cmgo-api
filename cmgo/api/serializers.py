from rest_framework.serializers import ModelSerializer, ReadOnlyField
from . import models


# class ActividadSerializer(Serializer):
#     month = CharField()
#     count = IntegerField()
class SlideImageSerializer(ModelSerializer):
    class Meta:
        model = models.SlideImage
        fields = '__all__'


class SlideSerializer(ModelSerializer):
    slides = SlideImageSerializer(many=True)

    class Meta:
        model = models.Slide
        fields = '__all__'
