# coding=utf-8
from django.http import JsonResponse ,HttpResponse
from jpspapp import function
import json
from .models import Club
from django.core import serializers


# Create your views here.

def club_list(request):
    data = serializers.serialize("json", Club.objects.all())
    response = JsonResponse(json.dumps(data), safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


