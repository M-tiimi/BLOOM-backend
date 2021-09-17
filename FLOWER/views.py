from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FLOWER.models import Flower
from FLOWER.serializers import FlowerSerializer
# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the FLOWER index.")

@api_view(['GET', "POST"])
def apitest(request):
    return Response("Hello I'm views")


@csrf_exempt
def flower_list(request):
    """
    List all code flowers, or create a new snippet.
    """
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



