from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FLOWER.models import Flower
from FLOWER.serializers import FlowerSerializer
from FLOWER.models import User
from FLOWER.serializers import UserSerializer
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
from FLOWER.form import UserForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from FLOWER.load_saved_model import make_predictions

#call ml-model and make a prediction that is shown on url ml-model
class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':                        
            prediction = make_predictions(""" niagara niagara ( r ) bob gosse's niagara niagara follows a blueprint not unlike a lot of young-lovers-on-the-road movies . 
wild marcy ( robin tunney ) and calm seth ( henry thomas ) meet cute , literally running into each other while shoplifting at a local store . 
a mere couple of scenes later , the two embark on a journey to toronto from their small , unnamed american town in pursuit of a rare doll that marcy desperately wants . 
along the way , true love inevitably blossoms . 
what sets niagara niagara apart , though , is that marcy is afflicted with tourette's syndrome , a neurological disorder that causes sudden muscle and vocal tics . 
tunney , displaying an acting range not hinted at in the teenage witch thriller the craft , delivers an astonishing performance that won her the best actress prize at last year's venice film festival . 
to term her work a tour-de-force is not to imply that she attacks the scenery ; tunney's effectiveness lies in her modulation and vulnerability , which makes her depiction of marcy's illness--which often causes her to act violently--that much more convincing and tragic . 
she and the nicely subtle thomas develop a sweetly innocent and beguilingly off-kilter chemistry . 
their journey hits a few rough spots creatively along the way , mostly the fault of writer matthew weiss . 
a detour involving a kindly widower ( michael parks ) who takes the couple in brings the story to a screeching halt , and the key character of a trigger-happy pharmacist ( stephen lang ) is highly unbelievable . 
but these missteps do not blunt the power of tunney's bravura turn , which carries niagara niagara to a level of poignance it would not have otherwise achieved . 
 ( opens march 20 ) 
 " i didn't know what to expect . 
it's like something you chase for so long , but then you don't know how to react when you get it . 
i still don't know how to react . " 
--michael jordan , on winning his first nba championship in 1991 . . . or , 
my thoughts after meeting him on november 21 , 1997  """)            
            response = {'prediction': prediction}           
            return JsonResponse(response)

class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'userform.html'

    def get(self, request, pk):
        pk =User.objects.get(pk=self.kwargs['pk'])
        user = get_object_or_404(User, pk=pk.id)
        
        serializer = UserSerializer(user)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        pk =User.objects.get(pk=self.kwargs['pk'])
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return HttpResponseRedirect('flower:userlist')


@csrf_exempt
def flower_list(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    


class UserList(APIView):
   
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


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

