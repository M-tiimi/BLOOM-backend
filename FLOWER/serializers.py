from rest_framework import serializers
from FLOWER.models import User
from FLOWER.models import Answer
from FLOWER.models import Question
from FLOWER.models import Task
from rest_framework_jwt.settings import api_settings



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    password =serializers.CharField(required = True, allow_blank=False)
    age = serializers.IntegerField(required=False)
    question = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    task = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    points = serializers.IntegerField()
   
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




class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

 
         



class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=40)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True) 
    answer = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        
        instance.save()
        return instance

class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    question =serializers.PrimaryKeyRelatedField(many=False, read_only= True)
   

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        
        
        instance.save()
        return instance

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    points=serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
   

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.points = validated_data.get('points', instance.points)
        
        
        instance.save()
        return instance