from rest_framework import serializers
from .models import CarModel,Data


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['Make_ID', 'Make_Name', 'Model_ID','Model_Name']

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['Count', 'Message', 'SearchCriteria','Results']