from rest_framework import serializers
from .models import General


# class GeneralSerializer(serializers.Serializer):
#     loadfile = serializers.CharField(max_length=25)
#     productionline = serializers.CharField(max_length=15)
#     ordernumber = serializers.CharField(max_length=15)
#     loadfiletime = serializers.DateTimeField()
#     datetimestart = serializers.DateTimeField()
#     datetimestop = serializers.DateTimeField()
#     r_mpurecipe = serializers.IntegerField()
#     r_recipenumber = serializers.IntegerField()
#     r_manufacturer = serializers.CharField(max_length=15)
#     r_type = serializers.CharField(max_length=15)
#     rawmatweightactual = serializers.FloatField(required=False)
#     operator = serializers.CharField(max_length=20, required=False)
#     comment = serializers.CharField(max_length=10, required=False)

#     def create(self, validated_data):
#         return General.objects.create(**validated_data)

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['datetimestart',
                  'datetimestop',
                  'ordernumber',
                  'productionline',
                  'r_mpurecipe',
                  'r_manufacturer',
                  'r_type',
                  'rawmatweightactual']

    def create(self, validated_data):
        return General.objects.create(**validated_data)
