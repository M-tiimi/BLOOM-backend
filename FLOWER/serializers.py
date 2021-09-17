from rest_framework import serializers
from FLOWER.models import Flower
from FLOWER.models import User
from FLOWER.models import Answer
from FLOWER.models import Question
from FLOWER.models import Task



class FlowerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    color = serializers.CharField(required=False, allow_blank=True, max_length=50)
    wellness = serializers.CharField(required=False, max_length = 100)

    def create(self, validated_data):
        
        #Create and return a new `Flower` instance, given the validated data.
        
        return Flower.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        #Update and return an existing `Flower` instance, given the validated data.
        
        instance.color = validated_data.get('color', instance.color)
        instance.wellness = validated_data.get('wellness', instance.wellness)
        
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    age = serializers.IntegerField(required=False)
  
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        
        instance.save()
        return instance

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=40)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        
        instance.save()
        return instance

class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=1000)
   

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        
        
        instance.save()
        return instance

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    points=serializers.IntegerField(read_only=True)
   

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.points = validated_data.get('points', instance.points)
        
        
        instance.save()
        return instance
