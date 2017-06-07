# coding=utf-8
from django.http import JsonResponse, HttpResponse
import json
from jpsp.shortcut import JPSPToken, JPSPTime
from jpspapp.models import Club, Post, Settings, Token
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate, login


def returnMessage(message):
    return JsonResponse({
        'message': message,
        'Access-Control-Allow-Origin': '*'
    })


# Create your views here.
@require_http_methods(['POST'])
def login(request):
    body = json.loads(request.body)
    username = body['Username']
    password = body['Password']
    user = authenticate(username=username, password=password)
    if user is not None:
        print("hello")
        login(request, username)
        return JsonResponse({
            "message": "User Authenticated",
            "Token": JPSPToken(username=username, usertype="club").generate(),
            "Access-Control-Allow-Origin": '*'
        })
    else:
        return JsonResponse({
            "message": "User Not Authenticated",
            "Access-Control-Allow-Origin": '*',
        })


@require_http_methods(['POST'])
def logout(request):
    try:
        body = json.loads(request)
        username = body['UserName']
        usertype = body['UserType']
        token_object = JPSPToken(username=username, usertype=usertype)
        token_object.remove()
    except:
        returnMessage(message='error')


@require_http_methods(["GET"])
def club_list(request):
    try:
        data = serializers.serialize("json", Club.objects.all())
        response = JsonResponse(json.dumps(data), safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    except:
        returnMessage(message='error')


@require_http_methods(["POST"])
def club_post_edit_submit(request):
    try:
        body = json.loads(request.body)
        clubname = body['ClubName']
        clubid = body['ClubId']
        linkman_grade = body['Linkman']['Grade']
        linkman_class = body['Linkman']['Class']
        linkman_name = body['Linkman']['Name']
        linkman_phonenumber = body['Linkman']['PhoneNumber']
        linkMan_qq = body['Linkman']['Qq']
        region = body['Region']
        date1 = body['Date1']
        content = body['Content']
        process = body['Process']
        assessment = body['Assessment']
        feeling = body['Feeling']
        token = body['Token']
        try:
            token_object = JPSPToken(username=clubid, usertype="club", token=token)
            # TODO: how to authenticate
            if token_object.authenticate():
                Post.objects.create(
                    ClubName=clubname,
                    ClubId=Club.objects.filter(clubid=clubid),
                    LinkmanGrade=linkman_grade,
                    LinkmanClass=linkman_class,
                    LinkmanName=linkman_name,
                    LinkmanPhoneNumber=linkman_phonenumber,
                    LinkmanQq=linkMan_qq,
                    Region=region,
                    Date1=date1,
                    Content=content,
                    Process=process,
                    Assessment=assessment,
                    Feeling=feeling,
                    Stars=0,
                    StarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            return JsonResponse(
                {
                    'message': 'Success',
                    'Access-Control-Allow-Origin': '*'
                }
            )
        except:
            return JsonResponse(
                {
                    'message': 'Error',
                    'Access-Control-Allow-Origin': '*'
                }
            )
    except:
        returnMessage(message='error')


@require_http_methods(["POST"])
def club_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage(message='error')


@require_http_methods(['GET'])
def club_recruit_classroom_apply_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        club_id = body['ClubId']
        club_name = body['ClubName']
        classroom = body['Classroom']
        date1 = body['Date1']
        date2 = body['Date2']
        date3 = body['Date3']
        returnMessage('success')
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_post_star_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_recruit_classroom_apply_verify_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def user_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_member_add_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_member_remove_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_message_list(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_message_remove_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_activity_apply_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        club_id = body['ClubId']
        club_name = body['ClubName']
        activity_name = body['ActivityName']
        region = body['Region']
        date1 = body['Date1']
        date2 = body['Date2']
        date3 = body['Date3']
        content = body['Content']
        type = body['Type']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_agree_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_list(request):
    try:
        body = json.loads(request.body)
        activity_list=Activity.object
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_disagree_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_post_delete_submit(request):
    try:
        body = json.loads(request.body)
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_establish(request):
    try:
        body = json.loads(request.body)
        clubname = body['Clubname']
        shezhang_name = body['Shezhang_Name']
        shezhang_qq = body['Shezhang-QQ']
        shezhang_grade = body['Shezhang_Grade']
        shezhang_classroom = body['Shezhang_Classroom']
        introduction = body['Introduction']
        if_recruit = body['IfRecruit']
        qq_group = body['QQGroup']
        email = body['Email']
        settings = Settings.objects.filter(name="settings")
        Club.objects.create(
            clubname=clubname,
            clubid=settings.clubid,
            shezhang_name=shezhang_name,
            shezhang_qq=shezhang_qq,
            shezhang_grade=shezhang_grade,
            shezhang_classroom=shezhang_classroom,
            if_recruit=if_recruit,
            introduction=introduction,
            email=email,
            # label
            state=False,
            achievements="",
            stars=0,
            enroll_group_qq=qq_group,
        )
        settings.cludid += 1
        settings.save()
        return JsonResponse(
            {
                'message': 'success',
                'Access-Control-Allow-Origin': '*'
            }
        )
    except:
        returnMessage('error')
