from django.db.models.fields.related import ForeignKey
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from FLOWER.models import User
from FLOWER.serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FLOWER.models import Answer, Task
from FLOWER.models import Question
from FLOWER.serializers import AnswerSerializer
from FLOWER.serializers import QuestionSerializer, TaskSerializer
from FLOWER.load_saved_model import make_predictions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.permissions import BasePermission
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return request.method 
        
#in developement...
class AllowUser(BasePermission):
    def has_permission(self, request, view):
        return request.method 
        
#Open Machine Learing API for making a prediction on text sentiment
@method_decorator(csrf_exempt, name='dispatch')
@api_view(['POST'])
@permission_classes([AllowAny])
def call_model(request):
    answer = request.data
    print(answer.get('data'))
    prediction = make_predictions(answer.get('data'))
    if (len(prediction) > 0):
        response = {'prediction': prediction}
        print(response)
        return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)
    else:
        return JsonResponse('error', status=status.HTTP_201_CREATED, safe=False)


#Autheticate and get user token and information about current user
@api_view(['POST'])
@permission_classes([User])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
  
#Create new user
@permission_classes([AllowAny])
class UserList(APIView):

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#Add new task for user
@permission_classes([AllowUser])
class TaskList(APIView):
  
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#returns user's tasks !!Authentication not required, in developement...
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_tasks(request, pk, format=None):
    #fix to return list of users tasks
    if request.method == 'GET':
        tasks = list(Task.objects.all().filter(user_id=pk))
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


#Modify or delete tasks, no url for this API, in developement...
@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])
def get_task_by_id(request, pk, format=None):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#get user's question, !!Authentication not required, in developement...
@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET'])
@permission_classes([AllowAny])
def get_question_by_id(request, pk, format=None):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)



  