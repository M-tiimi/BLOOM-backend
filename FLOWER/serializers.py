from rest_framework import serializers
from FLOWER.models import User
from FLOWER.models import Answer
from FLOWER.models import Question
from FLOWER.models import Task
from rest_framework_jwt.settings import api_settings


#Serializers allow data to be converted to native Python datatypes that can then be easily rendered into Json etc.
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    password =serializers.CharField(required = True, allow_blank=False)
    birth_year = serializers.IntegerField(read_only=True)
    email= serializers.EmailField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    points = serializers.IntegerField(required=False)
    task = serializers.PrimaryKeyRelatedField(many=True, required=False, allow_null = True, default=None, read_only=True)
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.birth_year = validated_data.get('birth_year', instance.birth_year)
        instance.email = validated_data.get('email', instance.email)
        instance.points = validated_data.get('points', instance.points)
        
        
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


    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'birth_year','points', 'email')    

 

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
    title = serializers.CharField(required=False, allow_blank=False, max_length=1000)
    user = UserSerializer(required=False)
   

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.get(**user_data)
        return Task.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        
        instance.save()
        return instance


