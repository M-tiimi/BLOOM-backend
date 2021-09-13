from rest_framework import serializers
from FLOWER.models import Flower


class FlowerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    color = serializers.CharField(required=False, allow_blank=True, max_length=50)
    wellness = serializers.CharField(required=False, max_length = 100)
    

    def create(self, validated_data):
        """
        Create and return a new `Flower` instance, given the validated data.
        """
        return Flower.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Flower` instance, given the validated data.
        """
        instance.color = validated_data.get('color', instance.color)
        instance.wellness = validated_data.get('wellness', instance.wellness)
        
        instance.save()
        return instance