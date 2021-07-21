from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Instrument, Brand




class InstrumentSerializer(ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'


class BrandSerializer(serializers.Serializer):
    class Meta:
        model = Brand,
        fields = '__all__'

