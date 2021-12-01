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


class AllowUser(BasePermission):
    def has_permission(self, request, view):
        return request.method         

#call ml-model and make a prediction that is shown on url ml-model
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


#authetication stuff
@api_view(['POST'])
@permission_classes([User])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
  


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
class TaskList(APIView):
  
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])
def get_task_by_id(request, pk, format=None):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])
def get_answer_by_id(request, pk, format=None):
    try:
        answer = Answer.objects.get(pk=pk)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  