from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myNLP.models import MyImdb, NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    MyImdb().imdb_process()
    return JsonResponse({'result': "imdb_process SUCCESS"})


@api_view(['GET'])
@parser_classes([JSONParser])
def web_scraping(request):
    NaverMovie().web_scraping()
    return JsonResponse({'result': "web_scraping SUCCESS"})


@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'result': "naver_process SUCCESS"})
