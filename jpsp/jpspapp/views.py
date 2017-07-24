# coding=utf-8
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.models import User
from jpsp.shortcut import JPSPToken, JPSPTime
from jpspapp.models import Club, Post, Token, Activity, Message, Classroom, LostAndFound, UserProfile, Cevent
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate


def cevent(request):
    body = json.loads(request.body)
    cusername = body['Username']
    content = body['Content']
    datetime1 = body['Datetime1']
    datetime2 = body['Datetime2']
    ctype = body['Type']
    Cevent.objects.create(cusername=cusername,content=content,ctype=ctype,datetime1=datetime1,datetime2=datetime2)
    return JsonResponse({
        'message': 'Success',
        'Access-Control-Allow-Origin': '*'
    })

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
                "UserName": Club(User.objects.get(username=userid)).ClubName,
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
def club_list(request):
    try:
        body = json.loads(request.body)
        type = body['Type']
        response = []
        club_object = None
        if type == 'Established':
            club_object = Club.objects.filter(State=True)
        elif type == 'Unestablished':
            club_object = Club.objects.filter(State=False)
        elif type == 'All':
            club_object = Club.objects.all()
        for data in club_object:
            response.append({'ClubId': data.ClubId,
                             'ClubName': data.ClubName,
                             'ShezhangName': data.ShezhangName,
                             'ShezhangQQ': data.ShezhangQq,
                             'ShezhangGrade': data.ShezhangGrade,
                             'ShezhangClassroom': data.ShezhangClass,
                             'IfRecruit': data.IfRecruit,
                             'EnrollGroupQQ': data.EnrollGroupQq,
                             'Email': data.Email,
                             'State': data.State,
                             'Stars': data.Stars,
                             'Introduction': data.Introduction,
                             'Achievements': data.Achievements,
                             })
            return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', data: json.dumps(response)},
                                safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def recruit_classroom_apply(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        club_id = body['ClubId']
        club_name = body['ClubName']
        date1 = body['Date1']
        date2 = body['Date2']
        # TODO: deal with date
        Classroom.objects.create(
            ClassroomId=0,
            ClubId=Club.objects.get(User.objects.get(username=club_id)),
            ClubName=club_name,
            Date1=date1,
            Date2=date2
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
def recruit_classroom_operate(request):
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
def recruit_classroom_list(request):
    pass


@require_http_methods(['POST'])
def club_member_operate(request):
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
def activity_apply(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        club_id = body['ClubId']
        activity_name = body['Name']
        region = body['Region']
        date1 = body['Date1']
        date2 = body['Date2']
        content = body['Content']
        type = body['Type']
        Activity.objects.create(
            ActivityName=activity_name,
            Region=region,
            Clubid=Club.objects.get(clubid=User.objects.get(username=club_id)),
            ClubName=Club.objects.get(clubid=User.objects.get(username=club_id)).ClubName,
            Content=content,
            Date1=date1,
            Date2=date2,
            State='0',
            Type=type,
            Participants=None
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
def activity_operate(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        activity_id = body['ActivityId']
        operation = body['Operation']
        if operation == 'Confirm':
            try:
                activity_object = Activity.objects.get(pk=activity_id)
                activity_object.State = 'Confirmed'
                activity_object.save()
            except:
                return JsonResponse({
                    'message': 'error',
                    'Access-Control-Allow-Origin': '*'
                })
        elif operation == 'UndoDeny':
            try:
                activity_object = Activity.objects.get(pk=activity_id)
                activity_object.State = 'Unconfirmed'
                activity_object.save()
            except:
                return JsonResponse({
                    'message': 'error',
                    'Access-Control-Allow-Origin': '*'
                })
        elif operation == 'Deny':
            try:
                activity_object = Activity.objects.get(pk=activity_id)
                activity_object.State = 'Denied'
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
def activity_list(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        type = body['Type']
        response = []
        activityList = None
        if type == 'All':
            activityList = Activity.objects.all()
        elif type == 'Past':
            activityList = Activity.objects.filter(Date2__lt=datetime.datetime.now())
        elif type == 'Happening':
            activityList = Activity.objects.filter(Date1__lte=datetime.datetime.now()).filter(
                Date2__gte=datetime.datetime.now())
        elif type == 'Future':
            activityList = Activity.objects.filter(Date1__gt=datetime.datetime.now())
        elif type == 'Unconfirmed':
            activityList = Activity.objects.filter(State='0')
        elif type == 'Confirmed':
            activityList = Activity.objects.filter(State='1')
        elif type == 'Denied':
            activityList = Activity.objects.filter(State='2')
        # TODO : token authenticate
        for data in activityList:
            response.append({
                'ActivityId': data.pk,
                'Name': data.Name,
                'Region': data.Region,
                # 'ClubId': data.ClubId,
                'ClubName': data.ClubName,
                'Content': data.Content,
                'Date1': str(data.Date1),
                'Date2': str(data.Date2),
                'State': data.State,
                'Type': data.Type
            })
        response_json = json.dumps(response)
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(["POST"])
def laf_submit(request):
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


@require_http_methods(["POST"])
def laf_list(request):
    try:
        body = json.loads(request.body)
        type = body['Type']
        response = []
        LostAndFoundList = None
        if type == 'Lost':
            LostAndFoundList = LostAndFound.objects.filter()
            # TODO: filter
        elif type == 'Found':
            LostAndFoundList = LostAndFound.objects.all()
            # TODO: filter
        elif type == 'Past':
            LostAndFoundList = LostAndFound.objects.all()
            # TODO: filter
        elif type == 'All':
            LostAndFoundList = LostAndFound.objects.all()
        for data in LostAndFoundList:
            response.append({
                'LostorFound': data.LostOrFound,
                'ObjectName': data.LostObjectName,
                'LinkmanGrade': data.LinkmanGrade,
                'LinkmanClass': data.LinkmanClass,
                'LinkmanPhoneNumber': data.LinkmanPhoneNumber,
                'LinkmanQq': data.LinkmanQq,
                'LinkmanName': data.LinkmanName,
                'Region': data.LostPlace,
                'Date1': data.LostDateTime,
                'Importance': data.Importacne,
                'Desc': data.Desc
            })
        response_json = json.dumps(response)
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(["POST"])
def post_submit(request):
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


@require_http_methods(['POST'])
def post_star(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        stars = body['Stars']
        post_id = body['PostId']
        try:
            post_object = Post.objects.get(pk=post_id)
            post_object.Stars = stars
            post_object.Pass = '2'
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


@require_http_methods(["POST"])
def post_list(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        type = body['Type']
        response = []
        post_object = None
        if type == 'UnStared':
            post_object = Post.objects.filter(Pass='0')
        elif type == "Stared":
            post_object = Post.objects.filter(Pass='2')
        elif type == "UnPassed":
            post_object = Post.objects.filter(Pass='1')
        elif type == "All":
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
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def post_operate(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        post_id = body['PostId']
        operation = body['Operation']
        if operation == 'Deny':
            try:
                post_object = Post.objects.get(pk=post_id)
                post_object.Pass = '1'
                post_object.Stars = '0.0'
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
        if operation == 'UndoDeny':
            try:
                post_object = Post.objects.get(pk=post_id)
                post_object.Pass = '0'
                post_object.Stars = '0.0'
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
def change_password(request):
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


@require_http_methods(['POST'])
def userprofile_get(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        userid = body['UserId']
        profile = UserProfile.objects.get()
        # TODO: get profile object
        response = {
            'UserName': profile.UserName,
            'Grade': profile.Grade,
            'Class': profile.Class,
            'AttendYear': profile.AttendYear,
            'QQ': profile.QQ,
            'Phone': profile.Phone,
            'Email': profile.Email
        }
        response_json = json.dumps(response)
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def userprofile_submit(request):
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
def clubprofile_get(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        clubid = body['ClubId']
        profile = Club.objects.get()
        # TODO: get profile object
        response = {
            'ClubName': profile.ClubName,
            'ShezhangName': profile.ShezhangName,
            'ShezhangQq': profile.ShezhangQq,
            'ShezhangGrade': profile.ShezhangGrade,
            'ShezhangClass': profile.ShezhangClass,
            'IfRecruit': profile.IfRecruit,
            'EnrollGroupQq': profile.EnrollGroupQq,
            'Email': profile.Email,
            'Label': profile.Label,
            'State': profile.State,
            'Stars': profile.Stars,
            'Introduction': profile.Introduction,
            'Achievements': profile.Achievements,
            'Member': profile.Member
        }
        response_json = json.dumps(response)
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(["POST"])
def clubprofile_submit(request):
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


@require_http_methods(["POST"])
def event_submit(request):
    pass


@require_http_methods(["POST"])
def event_list(request):
    pass


@require_http_methods(["GET"])
def club_page(request):
    pass


@require_http_methods(["POST"])
def club_page_setting(request):
    pass


@require_http_methods(["POST"])
def message_list(request):
    pass


def test(request):
    activityList = Activity.objects.filter(Date1__lt=datetime.datetime.now())
    for activity in activityList:
        return JsonResponse({'message': str(activity.Date1)})
