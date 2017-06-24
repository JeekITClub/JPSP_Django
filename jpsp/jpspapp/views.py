# coding=utf-8
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.models import User
from jpsp.shortcut import JPSPToken, JPSPTime
from jpspapp.models import Club, Post, Settings, Token, Activity, Message, Classroom, LostAndFound, UserProfile
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate



# Create your views here.
@require_http_methods(['POST'])
def login(request):
    body = json.loads(request.body)
    userid = body['UserName']
    password = body['Password']
    usertype = body['UserType']
    user = authenticate(username=userid, password=password)
    if user is not None:
        token_object = JPSPToken(username=userid, usertype=usertype)
        if usertype == "student":
            return JsonResponse({
                "UserName": UserProfile(User.objects.get(username=userid)).UserName,
                "message": "User Authenticated",
                "Token": token_object.generate(),
                "Access-Control-Allow-Origin": '*'
            })
        elif usertype == "Club":
            return JsonResponse({
                "UserName": Club(User.objects.get(username=userid)).clubname,
                "message": "User Authenticated",
                "Token": token_object.generate(),
                "Access-Control-Allow-Origin": '*'
            })
        elif usertype == "Club Department":
            return JsonResponse({
                "UserName": CDUser(User.objects.get(username=userid)).username,
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
        return JsonResponse({
            'message': 'success',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(["GET"])
def club_list(request):
    try:
        response = []
        club_object = Club.objects.all()
        for data in club_object:
            response.attend({'pk': data.pk,
                            'ClubName': data.ClubName,
                            'ShezhangName': data.ShezhangName,
                            'ShezhangQq': data.ShezhangQq,
                            'ShezhangGrade': data.ShezhangGrade,
                            'ShezhangClassroom': data.ShezhangClassroom,
                            'IfRecruit': data.IfRecruit,
                            'EnrollGroupQq': data.EnrollGroupQq,
                            'Email': data.Label,
                            'State': data.State,
                            'Stars': data.Stars,
                            'Introduction': data.Introduction,
                            'Achievements': data.Achievements,
                            #'Member'
            })
            response_json = json.dumps(response)
            return JsonResponse(response_json, safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


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
                    StarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    Pass=False
                )
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


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
            club_object.Clubname = clubname
            club_object.ShezhangName = shezhang_name
            club_object.ShezhangGrade = shezhang_grade
            club_object.ShezhangClassroom = shezhang_class
            club_object.ShezhangQq = shezhang_qq
            club_object.IfRecruit = if_recruit
            club_object.EnrollGroupQq = enroll_group_qq
            club_object.Email = email
            club_object.Label = label
            club_object.State = state
            club_object.Introduction = introduction
            club_object.Achievements = achievements
            club_object.save()
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['GET'])
def club_recruit_classroom_apply_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        club_id = body['ClubId']
        club_name = body['ClubName']
        date1 = body['Date1']
        date2 = body['Date2']
        date3 = body['Date3']
        # TODO: deal with date
        Classroom.objects.create(
            ClassroomId=0,
            ClubId=Club.objects.get(User.objects.get(username=club_id)),
            ClubName=club_name,
            # Date1=date1 + date2,
            # Date2=date1 + date3
            # TODO: deal with date
        )
        return JsonResponse({
            'message': 'success',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_post_star_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        stars = body['Stars']
        post_id = body['PostId']
        try:
            post_object = Post.objects.get(pk=post_id)
            post_object.Stars = stars
            post_object.IfPass = True
            post_object.save()
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_recruit_classroom_apply_verify_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        classroom = body['Classroom']
        clubid = body['ClubId']
        # date
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def user_profile_edit_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        classroom = body['Classroom']
        grade = body['Grade']
        attend_year = body['AttendYear']
        try:
            user_profile_object = UserProfile.objects.get()
            return JsonResponse({
            'message': 'success',
            'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def club_member_add_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        club_id = body['ClubId']
        userid = body['userid']
        club_object = Club.objects.get(Club)
        # userid 为学生账号 为学号  数字
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def club_member_remove_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']

        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_message_list(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        response = []
        # message_object = Message.objects.filter(ToUser=)
        #  TODO: message_object !
        for data in message_object:
            response.append({'pk': data.pk,
                            'FromUser': data.FromUser,
                            'ToUser': data.ToUser,
                            'Type': data.Type,
                            'Content': data.Content
                            })
        response_json = json.dumps(response)
        return JsonResponse(response_json, safa=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_message_remove_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        message_id = body['MessageId']
        if body['ToUser'] == 'Club Department':
            try:
                message_object = Message.objects.filter(ToUser=to_user)
                message_object.remove()
                return JsonResponse({
                    'message': 'success',
                    'Access-Control-Allow-Origin': '*'
                })
            except:
                return JsonResponse({
                    'message': 'error',
                    'Access-Control-Allow-Origin': '*'
                })
        else:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


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
            State='0',
            Type=type,
            Participants=''
        )
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_activity_agree_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        activity_id = body['ActivityId']
        try:
            activity_object = Activity.objects.get(pk=activity_id)
            activity_object.state = '1'
            activity_object.save()
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_activity_list(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        # TODO : token authenticate
        for num in range(0, Activity.objects.all().count()):
            for data in Activity.objects.all():
                return JsonResponse({
                    str(num): {
                        'ActivityId': data.pk,
                        'ActivityName': data.ActivityName,
                        'Region': data.Region,
                        'ClubId': data.ClubId,
                        'ClubName': data.ClubName,
                        'Content': data.Content,
                        'Date1': data.Date1,
                        'Date2': data.Date2,
                        'State': data.State,
                        'Type': data.Type
                    }
                })

    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_activity_deny_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        acitivity_id = body['AcitivityId']
        try:
            activity_object = Activity.objects.get(pk=acivity_id)
            activity_object.state = '2'
            activity_object.save()
            # 2-> denied
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def cd_post_deny_submit(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        post_id = body['PostId']
        try:
            post_object = Post.objects.get(pk=post_id)
            post_object.IfPass = False
            post_object.save()
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def club_establish(request):
    try:
        body = json.loads(request.body)
        clubname = body['Clubname']
        shezhang_name = body['Shezhang_Name']
        shezhang_qq = body['Shezhang_QQ']
        shezhang_grade = body['Shezhang_Grade']
        shezhang_classroom = body['Shezhang_Classroom']
        introduction = body['Introduction']
        if_recruit = body['IfRecruit']
        qq_group = body['QQGroup']
        email = body['Email']
        #
        # settings = Settings.objects.filter(name="settings")
        Club.objects.create(
            Clubname=clubname,
            # TODO: ClubId
            ShezhangName=shezhang_name,
            SheZhangQq=shezhang_qq,
            ShezhangGrade=shezhang_grade,
            ShezhangClassroom=shezhang_classroom,
            IfRecruit=if_recruit,
            Introduction=introduction,
            Email=email,
            # TODO: label!
            State=False,
            Achievements="",
            Stars=0,
            EnrollGroupQq=qq_group,
        )
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(["POST"])
def lost_and_found_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        lostOrFound = body['LostOrFound']
        objectName = body['ObjectName']
        linkmanName = body['LinkmanName']
        linkmanGrade = body['LinkmanGrade']
        linkmanPhoneNumber = body['LinkmanPhoneNumber']
        linkmanClass = body['LinkmanClass']
        linkmanQq = body['LinkmanQq']
        region = body['Region']
        date1 = body['Date1']
        date2 = body['Date2']
        importance = body['Importance']
        desc = body['Desc']
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
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
        except:
            return JsonResponse({
                'message': 'error',
                'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


# TODO: CHANGE INTO POST!!!
@require_http_methods(["GET"])
def cd_post_list(request):
    try:
        # body = json.loads(request.body)
        # token = body['Token']
        response = []
        post_object = Post.objects.all()
        for data in post_object:
            response.append({'pk': data.pk,
                             'ClubName': data.ClubName,
                             'LinkmanGrade': data.LinkmanGrade,
                             'LinkmanPhoneNumber': data.LinkmanPhoneNumber,
                             'LinkmanName': data.LinkmanName,
                             'LinkmanQq': data.LinkmanQq,
                             'Region': data.Region,
                             'Date1': str(data.Date1),
                             'Date2': str(data.Date2),
                             'Process': data.Process,
                             'Content': data.Content,
                             'Assessment': data.Assessment,
                             'Feeling': data.Feeling,
                             'Stars': data.Stars
                             })
        response_json = json.dumps(response)

        return JsonResponse({'message': 'success','Access-Control-Allow-Origin': '*','data': response_json}, safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def change_password_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        password = body['Password']
        userid = body['UserId']
        try:
            pass
        except:
            return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
            })
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })
