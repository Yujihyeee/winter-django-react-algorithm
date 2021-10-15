from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.crawling.models import Crawling


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crawling().process()
    return JsonResponse({'result': "Success"})


@api_view(['GET'])
@parser_classes([JSONParser])
def tweet(request):
    Crawling().tweet_trump()
    return JsonResponse({'result': "Success"})
