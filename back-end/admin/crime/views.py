from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result': "Create Police Position SUCCESS"})


@api_view(['GET'])
@parser_classes([JSONParser])
def create_cctv_model(request):
    CrimeCctvModel().create_cctv_model()
    return JsonResponse({'result': "Create CCTV model Success"})


@api_view(['GET'])
@parser_classes([JSONParser])
def create_population_model(request):
    CrimeCctvModel().create_population_model()
    return JsonResponse({'result': "Create Population model Success"})
