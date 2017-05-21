# coding=utf-8
from django.http import JsonResponse, HttpResponse
from jpspapp import function
import json
from .models import Club, Post
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime


# Create your views here.
@require_http_methods(["GET"])
def club_list(request):
    data = serializers.serialize("json", Club.objects.all())
    response = JsonResponse(json.dumps(data), safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response


@require_http_methods(["POST"])
def club_post_edit_submit(request):
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
    assessment = body['Assessment']
    feeling = body['Feeling']
    # Post.objects.create(
    #     #ClubName=Club.objects.filter(name=clubname),
    #     LinkmanGrade=linkman_grade,
    #     LinkmanClass=linkman_class,
    #     LinkmanName=linkman_name,
    #     LinkmanPhoneNumber=linkman_phonenumber,
    #     LinkmanQq=linkMan_qq,
    #     Region=region,
    #     #Date1=date1,
    #     #Date2=date2,
    #     Content=content,
    #     Process=process,
    #     Assessment=assessment,
    #     Feeling=feeling,
    #     Stars=0,
    #     StarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # )
    return JsonResponse(
        {
            'message': 'success',
            'Access-Control-Allow-Origin': '*'
        }
    )


@require_http_methods(["POST"])
def club_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['GET'])
def club_recruit_classroom_apply_submit(request):
    try:
        body = json.loads(request.body)
        Token = body['Token']
        if Token:
            clubname = body['ClubName']
            classroom = body['Classroom']
            date1 = body['Date1']
            date2 = body['Date2']
            date3 = body['Date3']

    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_post_star_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_recruit_classroom_apply_verify_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def user_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def club_member_add_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def club_member_remove_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_message_list(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_message_remove_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def club_activity_apply_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_activity_agree_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )
    finally:
        pass


@require_http_methods(['POST'])
def cd_activity_list(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_activity_disagree_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )


@require_http_methods(['POST'])
def cd_post_delete_submit(request):
    try:
        body = json.loads(request.body)
    except:
        return JsonResponse(
            {
                'message': ''
            }
        )
