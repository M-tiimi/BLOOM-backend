from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FLOWER.models import Flower
from FLOWER.serializers import FlowerSerializer
from FLOWER.models import User
from FLOWER.serializers import UserSerializer, UserSerializerWithToken
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FLOWER.models import Answer
from FLOWER.models import Question
from FLOWER.serializers import AnswerSerializer
from FLOWER.serializers import QuestionSerializer
from django.shortcuts import render
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from FLOWER.load_saved_model import make_predictions
from rest_framework.decorators import api_view
from rest_framework import permissions, status

#call ml-model and make a prediction that is shown on url ml-model
class call_model(APIView):
    
    def get(self,request):
        data = Answer.objects.get(id=2)
        print(data.title)
        if request.method == 'GET':                        
            prediction = make_predictions("I hate life")            
            response = {'prediction': prediction}           
            return JsonResponse(response)


#authetication stuff
@api_view(['GET'])
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

