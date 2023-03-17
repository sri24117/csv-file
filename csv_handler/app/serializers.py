from rest_framework import serializers
from app.models import DataModel

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'

class SortedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = ('column1', 'column2', 'column3', ...) 