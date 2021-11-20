from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from FLOWER.models import Flower
from FLOWER.serializers import FlowerSerializer
from FLOWER.models import User
from FLOWER.serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FLOWER.models import Answer
from FLOWER.models import Question
from FLOWER.serializers import AnswerSerializer
from FLOWER.serializers import QuestionSerializer
from FLOWER.load_saved_model import make_predictions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.permissions import BasePermission
from django.utils.decorators import method_decorator



class AllowAny(BasePermission):
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
        return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)
    else:
        return JsonResponse('error', status=status.HTTP_201_CREATED, safe=False)
    

#authetication stuff
@api_view(['POST'])
@permission_classes([User])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)



class FlowerList(APIView):
    def get(self, request, format=None):
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)   


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    

#class based view of Questions returns all Questions from database in JSON
class QuestionList(APIView):
   
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class AnswerList(APIView):
   
    def get(self, request, format=None):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

