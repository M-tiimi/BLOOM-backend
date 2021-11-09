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
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from FLOWER.load_saved_model import make_predictions

#call ml-model and make a prediction that is shown on url ml-model
class call_model(APIView):
    
    def get(self,request):
        data = Answer.objects.get(id=2)
        print(data.title)
        if request.method == 'GET':                        
            prediction = make_predictions("""plot : a dude and his brother are driving cross-country and decide to fool around with a trucker on their cb radio . 
it isn't long before their little prank gets someone put into a coma ( long story ) and the next thing you know , the trucker is following them too . 
lotsa nuttiness ensues and then , they pick up their other friend , venna , a girl who the dude has a crush on . 
but what's this . . . ? 
the trucker is still on their tail and is now harassing all three of the young whippersnappers . . . ? 
you bet ! 
buckle up , dorothy . . . this is gonna be one bumpy ride ! 
critique : a good ol' time at the movies ! 
here's a film that actually gives away most of its plotline in its trailer and doesn't really bring anything " new " to the forefront ( if you've seen flicks like duel and breakdown , you've crossed this path before ) , but still manages to entertain you gangbusters , with realistic situations , believable characters , funny moments , thrills , chills , the whole shebang . 
let's give it up for director john dahl , who continues to put out solid films every other year ( if you haven't seen red rock west , do yourself a favor right now , and jot it down on a piece of paper and rent it at your earliest convenience ) . 
and much like that film , this one has an excellent premise and sets everything up at an even pace . 
it gives you a little bit of background on each of the main three characters , and then shows you how one small prank , can lead to a whole lotta trouble for everyone ! 
paul walker really surprised me in this movie , since i've never much thought of him as anything more than a pretty face ( and damn , is it ever pretty or what ? ! ) 
but here , he actually manages to put some depth behind the looks and that's always appreciated in films in which you are so closely tied to the main characters . 
sobieski is also good , but she isn't in the movie for as long as you'd think , but the man who really takes this film to another level , is steve zahn . 
if you've loved this guy as the " goofball " in most of his previous roles , you'll appreciate him even more here , as the dude who starts off as one of the most manic and excited human beings i've seen in quite some time ( " this is so awesome ! ! " ) , 
only to turn into a man scared out of his wits by the end of the flick . 
and speaking of the ending , boy , does this movie deliver some chilling moments during its final 15 clicks or what ? ! ? 
the arrow and i were practically in each others arms ( well , maybe i'm exaggerating , but you catch my drift ) as each minute brought about another turn of events which in turn , took it all to an even higher level . 
once again , kudos to director dahl for being able to generate that type of intensity , suspense and tension , with a great score , editing , style and camerawork . 
plot-wise , i too did wonder how the " bad guy " was able to track them so well , but it didn't really bother me all that much ( you can assume that he had bugged their car ? ) . 
but pretty much everything else in the story stuck like glue and i couldn't help but put myself in their shoes and appreciate their thoroughly desperate circumstance . 
a great movie with an even cooler ending , this film will likely be remembered as one of the better thrillers of the year . 
 " this is amazing ! ! ! " 
where's joblo coming from ? 
american psycho ( 10/10 ) - deep blue sea ( 8/10 ) - eye of the beholder ( 4/10 ) - the fast and the furious ( 7/10 ) - final destination ( 8/10 ) - the glass house ( 6/10 ) - no way out ( 8/10 )  """)            
            response = {'prediction': prediction}           
            return JsonResponse(response)


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

