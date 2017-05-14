# coding=utf-8
from django.http import JsonResponse, HttpResponse
from jpspapp import function
import json
from .models import Club, Post
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime


# Create your views here.

def club_list(request):
    data = serializers.serialize("json", Club.objects.all())
    response = JsonResponse(json.dumps(data), safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


@require_http_methods(["POST"])
def PostEditSubmit(request):
    try:
        body = json.loads(request.body)
        clubname = body['ClubName']
        linkman_grade = body['Linkman']['Grade']
        linkman_class = body['Linkman']['Class']
        linkman_name = body['Linkman']['Name']
        linkman_phonenumber = body['Linkman']['PhoneNumber']
        linkMan_qq = body['Linkman']['Qq']
        region = body['Region']
        date1 = body['Date1']
        date2 = body['Date2']
        content = body['Content']
        process = body['Process']
        assessment = body['Assessement']
        feeling = body['Feeling']
        Post.objects.create(
            ClubName=clubname,
            LinkmanGrade=linkman_grade,
            LinkmanClass=linkman_class,
            LinkmanName=linkman_name,
            LinkmanPhoneNumber=linkman_phonenumber,
            LinkmanQq=linkMan_qq,
            Region=region,
            Date1=date1,
            Date2=date2,
            Content=content,
            Process=process,
            Assessment=assessment,
            Feeling=feeling,
            Stars=0,
            StarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return JsonResponse(
            {
                'message': 'success',
                'Access-Control-Allow-Origin': '*'
            }
        )
    except:
        return JsonResponse(
            {
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            }
        )