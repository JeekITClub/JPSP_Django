# coding=utf-8
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.models import User
from jpsp.shortcut import JPSPToken, JPSPTime
from jpspapp.models import Club, Post, Settings, Token, Activity, Message, Classroom, LostAndFound
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate


def returnMessage(message):
    return JsonResponse({
        'message': message,
        'Access-Control-Allow-Origin': '*'
    })


# Create your views here.
@require_http_methods(['POST'])
def login(request):
    body = json.loads(request.body)
    username = body['UserName']
    password = body['Password']
    user = authenticate(username=username, password=password)
    if user is not None:
        token_object = JPSPToken(username=username, usertype="club")
        return JsonResponse({
            "message": "User Authenticated",
            "Token": token_object.generate(),
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
        linkman_grade = body['LinkmanGrade']
        linkman_class = body['LinkmanClass']
        linkman_name = body['LinkmanName']
        linkman_phonenumber = body['LinkmanPhoneNumber']
        linkMan_qq = body['LinkmanQq']
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
        token = body['Token']
        clubid = body['clubid']
        clubname = body['clubname']
        shezhang_name = body['shezhang_name']
        shezhang_qq = body['shezhang_qq']
        shezhang_grade = body['shezhang_grade']
        shezhang_class = body['shezhang_class']
        if_recruit = body['if_recruit']
        enroll_group_qq = body['enroll_group_qq']
        email = body['email']
        label = body['label']
        state = body['state']
        introduction = body['introduction']
        achievements = body['achievements']
        try:
            club_object = Club.objects.get(clubid=clubid)
            club_object.clubname = clubname
            club_object.shezhang_name = shezhang_name
            club_object.shezhang_grade = shezhang_grade
            club_object.shezhang_classroom = shezhang_class
            club_object.shezhang_qq = shezhang_qq
            club_object.if_recruit = if_recruit
            club_object.enroll_group_qq = enroll_group_qq
            club_object.email = email
            club_object.label = label
            club_object.state = state
            club_object.introduction = introduction
            club_object.achievements = achievements
            club_object.save()
            returnMessage(message='success')
        except:
            returnMessage(message='error')
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
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_recruit_classroom_apply_verify_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def user_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_member_add_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def club_member_remove_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_message_list(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_message_remove_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
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
        content = body['Content']
        type = body['Type']
        Activity.objects.create(
            ActivityName=activity_name,
            Region=region,
            Clubid=Club.objects.get(clubid=User.objects.get(username=club_id)),
            ClubName=club_name,
            Content=content,
            Date1=date1,
            Date2=date2,
            state='0',
            Type=type
        )
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_agree_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_list(request):
    try:
        body = json.loads(request.body)
        token= body['token']
        # TODO : token authenticate
        data=serializers.serialize("json",Activity.objects.filter(state='0'))
        response= JsonResponse(json.dumps(data),safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['message']='success'
        return response
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_activity_disagree_submit(request):
    try:
        body = json.loads(request.body)
        token=body['token']
    except:
        returnMessage('error')


@require_http_methods(['POST'])
def cd_post_delete_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
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


@require_http_methods(["POST"])
def lost_and_found_submit(request):
    try:
        body=json.loads(request.body)
        token=body['Token']
        lostOrFound=body['LostOrFound']
        objectName=body['ObjectName']
        linkmanName=body['LinkmanName']
        linkmanGrade = body['LinkmanGrade']
        linkmanPhoneNumber = body['LinkmanPhoneNumber']
        linkmanClass = body['LinkmanClass']
        linkmanQq = body['LinkmanQq']
        region = body['Region']
        date1= body['Date1']
        date2 = body['Date2']
        importance=body['Importance']
        desc=body['Desc']
        try:
            LostAndFound.objects.create(
                LostOrFound=lostOrFound,
                LinkmanName=linkmanName,
                LinkmanGrade=linkmanGrade,
                LinkmanClassroom=linkmanClass,
                LinkmanPhoneNumber=linkmanPhoneNumber,
                LinkmanQq=linkmanQq,
                LostObjectName=objectName,
                LostPlace=region,
                Importance=importance,
                Desc=desc,
                LostDateTime=date1
            )
            returnMessage(message='success')
        except:
            returnMessage(message='error')
    except:
        returnMessage(message='error')

@require_http_methods(["POST"])
def cd_post_list(request):
    try:
        # body=json.loads(request.body)
        # token=body['Token']
        querySet=Post.objects.all()
        response=[]
        for num in range(0,querySet.count()):
            for data in querySet:
                response[num]['PostId']=data.pk
                response[num]['ClubName']=data.ClubName
                response[num]['ClubId']=data.ClubId.clubid.username
                response[num]['LinkmanGrade']=data.LinkmanGrade
                response[num]['LinkmanName']=data.LinkmanName
                response[num]['LinkmanPhoneNumber'] = data.LinkmanPhoneNumber
                response[num]['LinkmanQq'] = data.LinkmanQq
                response[num]['Region']=data.Region
                response[num]['Date1'] = data.Date1
                response[num]['Date2'] = data.Date2
                response[num]['Process'] = data.Process
                response[num]['Content'] = data.Content
                response[num]['Assessment'] = data.Assessment
                response[num]['Feeling'] = data.Feeling
                response[num]['Stars'] = data.Stars
                response[num]['StarTime'] = data.StarTime
    except:
        returnMessage(message='error')