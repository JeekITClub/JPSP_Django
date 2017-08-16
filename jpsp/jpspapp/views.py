# coding=utf-8
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from jpspapp.models import Club, Post, Token, Activity, Classroom, LostAndFound, UserProfile, CDUser, \
    ActivityParticipantShip, ClubMemberShip
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate
import itchat
import random
from django.core.paginator import Paginator
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


def token_generate(user_id):
    token = ""
    for i in range(30):
        token += alphabet[random.randint(0, len(alphabet) - 1)]
    try:
        Token.objects.create(
            Token=token,
            UserObject=User.objects.get(username=user_id)
        )
    except:
        token_object = Token.objects.get(UserObject=User.objects.get(username=user_id))
        token_object.Token = token
        token_object.save()
    finally:
        return token


def token_authenticate(user_id, token):
    try:
        token_objects = Token.objects.get(UserObject=User.objects.get(username=user_id))
        if token_objects.Token == token:
            return True
        else:
            return False
    except:
        return False


def token_remove(user_id):
    try:
        Token.objects.get(UserObject=User.objects.get(username=user_id)).delete()
        return True
    except:
        return False


# Create your views here.

@require_http_methods(['POST'])
def login(request):
    global token_object
    try:
        body = json.loads(request.body)
        user_id = body['UserName']
        password = body['Password']
        usertype = body['UserType']
        user = authenticate(username=user_id, password=password)
        if user is not None:
            if usertype == "Student":
                object = UserProfile.objects.get(UserObject=User.objects.get(username=user_id))
                return JsonResponse({
                    "UserName": object.UserName,
                    "message": "User Authenticated",
                    "Token": token_generate(user_id=user_id),
                    "Access-Control-Allow-Origin": '*'
                })
            elif usertype == "Club":
                object = Club.objects.get(ClubObject=User.objects.get(username=user_id))
                return JsonResponse({
                    "UserName": object.ClubName,
                    "message": "User Authenticated",
                    "Token": token_generate(user_id=user_id),
                    "Access-Control-Allow-Origin": '*'
                })
            elif usertype == "CD":
                # TODO: CDUser
                object = CDUser.objects.get()
                return JsonResponse({
                    "UserName": CDUser(User.objects.get(username=user_id)).UserName,
                    "message": "User Authenticated",
                    "Token": token_generate(user_id=user_id),
                    "Access-Control-Allow-Origin": '*'
                })
    except:
        return JsonResponse({
            "message": "User Not Authenticated",
            "Access-Control-Allow-Origin": '*',
        })


@require_http_methods(['POST'])
def logout(request):
    try:
        body = json.loads(request)
        user_id = body['UserId']
        if token_remove(user_id):
            return JsonResponse({
                'message': 'success',
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


# 社团部访问接口
@require_http_methods(['POST'])
def club_list(request):
    try:
        body = json.loads(request.body)
        type = body['Type']
        token = body['Token']
        # TODO: !!
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

@require_http_methods(['GET'])
def club_show(request):
    try:
        response = []
        club_object = Club.objects.filter(State=True)
        paginator = Paginator(club_object,1)
        page = request.GET.get('Page')
        club_object_page = paginator.page(page)
        for data in club_object_page:
            if not data.IfRecruit:
                response.append({'ClubId': data.ClubId,
                                 'ClubName': data.ClubName,
                                 'Type': data.Type,
                                 'IfRecruit': 'False',
                                 })
            elif data.IfRecruit:
                response.append({'ClubId': str(data.ClubId),
                                 'ClubName': str(data.ClubName),
                                 'Type': data.Type,
                                 'IfRecruit': 'True',
                                 })
        return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': json.dumps(response)},
                            safe=False)
    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def club_attend(request):
    try:
        body = json.loads(request.body)
        token = body['IndexToken']
        club_id = body['ClubId']
        user_id = body['UserId']
        if (token_authenticate(user_id=user_id,token=token)):
            return JsonResponse({
                'message': 'success',
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
def club_quit(request):
    try:
        body = json.loads(request.body)
        token = body['IndexToken']
        user_id = body['UserId']
        club_id = body['ClubId']
        if(token_authenticate(user_id=user_id,token=token)):
            ClubMemberShip.objects.get(Member=UserProfile.objects.get(UserObject=User.objects.get(username=user_id)),Club=Club.objects.get(ClubId=club_id)).delete()
        return True
    except:
        return False


@require_http_methods(['POST'])
def club_member_add(request):
    try:
        body = json.loads(request.body)
        # club_id -> example: '303'
        club_id = body['ClubId']
        token = body['Token']
        # username -> example: 'S320150181'
        username = body['UserName']
        if(token_authenticate(user_id=club_id,token=token)):
            ClubMemberShip.objects.create(Member=UserProfile.objects.get(UserObject=User.objects.get(username=username)),Club=Club.objects.get(ClubId=club_id))
            return JsonResponse({
                'message': 'success',
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
def club_confirmed_member_list(request):
    try:
        # TODO: how to identify confirmed and unconfirmed
        body = json.loads(request.body)
        token = body['Token']
        # club_id -> example: '303'
        club_id = body['ClubId']
        if (token_authenticate(user_id=club_id,token=token)):
            membership_set = ClubMemberShip.objects.filter(Club=Club.objects.get(ClubId=club_id)).filter(State=1)
            response = []
            for membership in membership_set:
                response.append({
                    'UserName': membership.Member.UserName,
                    'Class': membership.Member.Class,
                    'Grade': membership.Member.Grade,
                    'AttendYear': membership.Member.AttendYear,
                    'Phone': membership.Member.Phone,
                    'QQ': membership.Member.QQ
                })
            response_json = json.dumps(response)
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*',
                'data': response_json
            }, safe=False)
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
def club_unconfirmed_member_list(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        # club_id -> example: '303'
        club_id = body['ClubId']
        if (token_authenticate(user_id=club_id,token=token)):
            membership_set = ClubMemberShip.objects.filter(Club=Club.objects.get(ClubId=club_id)).filter(State=0)
            response = []
            for membership in membership_set:
                response.append({
                    'UserName': membership.Member.UserName,
                    'Class': membership.Member.Class,
                    'Grade': membership.Member.Grade,
                    'AttendYear': membership.Member.AttendYear,
                    'Phone': membership.Member.Phone,
                    'QQ': membership.Member.QQ
                })
            response_json = json.dumps(response)
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*',
                'data': response_json
            }, safe=False)
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
    try:
        body = json.loads(request.body)
        token = body['Token']
        type = body['Type']
        response = []
        if type == 'Confirmed':
            pass
        elif type == 'Denied':
            pass
        elif type == 'Unconfirmed':
            pass
        elif type == 'All':
            classroom_objects_set = Classroom.objects.all()
            # TODO: !!!!!!!
            for classroom in classroom_objects_set:
                response.append({})
        response_json = json.dumps(response)
        return JsonResponse({
            'message': 'success',
            'Access-Control-Allow-Origin': '*',
            'data': response_json
        }, safe=False)

    except:
        return JsonResponse({
            'message': 'error',
            'Access-Control-Allow-Origin': '*'
        })


@require_http_methods(['POST'])
def club_member_remove(request):
    try:
        body = json.loads(request.body)
        token = body['token']
        # club_id -> example: '303'
        club_id = body['ClubId']
        # username -> example: 'S320150181'
        user_id = body['UserId']
        if(token_authenticate(user_id=club_id,token=token)):
            ClubMemberShip.objects.get(Club=Club.objects.get(ClubId=club_id), Member=UserProfile.objects.get(
                UserObject=User.objects.get(username=user_id))).delete()
            return JsonResponse({
                'message': 'success',
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
            Type=type
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
def activity_attend(requset):
    try:
        body = json.loads(requset.body)

        # token = body['Token']
        # activity_id -> int
        activity_id = body['ActivityId']
        # user_id -> str
        user_id = body['UserId']
        ActivityParticipantShip.objects.create(Activity=Activity.objects.get(pk=activity_id),
                                               Participant=UserProfile.objects.get(
                                                   UserObject=User.objects.get(username=user_id)))
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
def activity_detail(request):
    try:
        body = json.loads(request.body)
        # activity_id -> int
        activity_id = body['ActivityId']
        activity = Activity.objects.get(pk=1)
        return JsonResponse({
            'message': 'success',
            'Access-Control-Allow-Origin': '*',
            'data': {
                'Name': activity.Name,
                'Region': activity.Region,
                'ClubName': activity.ClubObject.ClubName,
                'Content': activity.Content,
                'Date1': str(activity.Date1),
                'Date2': str(activity.Date2),
            }
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
                return JsonResponse({
                    'message': 'success',
                    'Access-Control-Allow-Origin': '*'
                })
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
            token_object = JPSPToken(username=clubid, token=token)
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
        token = body['CDToken']
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
        user_id = body['UserId']
        if token_authenticate(user_id=user_id, token=token):
            profile = UserProfile.objects.get(UserObject=User.objects.get(username=user_id))
            club_set = profile.club_set
            activity_set = profile.activity_set
            club_tuple = []
            if club_set.count() > 0:
                for club in club_set:
                    club_tuple.append(club.ClubName)
            act_future_set = []
            act_past_set = []
            act_now_set = []
            now = datetime.datetime.now()
            if activity_set.count() >0:
                for activity in activity_set:
                    if activity.Date2 <= now:
                        act_past_set.append(activity.Name)
                    elif activity.Date1 >= now:
                        act_future_set.append(activity.Name)
                    elif activity.Date1 <= now <= activity.Date2:
                        act_now_set.append(activity.Name)
            response = {
                'UserName': profile.UserName,
                'Grade': profile.Grade,
                'Class': profile.Class,
                'AttendYear': profile.AttendYear,
                'QQ': profile.QQ,
                'Phone': profile.Phone,
                'Email': profile.Email,
                'Club': club_tuple,
                'ActNow': act_now_set,
                'ActPast': act_past_set,
                'ActFuture': act_future_set
            }
            response_json = json.dumps(response)
            return JsonResponse({
                'message': 'success',
                'Access-Control-Allow-Origin': '*',
                'data': response_json
            }, safe=False)
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


# noinspection PyBroadException
@require_http_methods(['POST'])
def userprofile_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        user_id = body['UserId']
        if(token_authenticate(user_id=user_id,token=token)):
            username = body['UserName']
            classroom = body['Class']
            # 不能使用class 因为是关键字
            grade = body['Grade']
            # attend_year = body['AttendYear']
            qq = body['QQ']
            email = body['Email']
            phone = body['Phone']
            attend_year = body['AttendYear']
            # upo -> user profile object
            upo = UserProfile.objects.get(UserObject=User.objects.get(username=user_id))
            upo.UserName = username
            upo.Class = classroom
            upo.Grade = grade
            upo.QQ = qq
            upo.Email = email
            upo.Phone = phone
            upo.AttendYear = attend_year
            upo.save()
            return JsonResponse({
                'message': 'success',
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


@require_http_methods(['GET'])
def club_profile_get(request):
    try:
        body = json.loads(request.body)
        clubid = body['ClubId']
        profile = Club.objects.get(ClubId=clubid)
        response = None
        if profile.IfRecruit:
            response = {
                'ClubName': profile.ClubName,
                'ShezhangName': profile.ShezhangName,
                'ShezhangQq': profile.ShezhangQq,
                'ShezhangGrade': profile.ShezhangGrade,
                'ShezhangClass': profile.ShezhangClass,
                'IfRecruit': 'False',
                'EnrollGroupQq': profile.EnrollGroupQq,
                'Email': profile.Email,
                'Label': profile.Label,
                'State': profile.State,
                'Stars': profile.Stars,
                'Introduction': profile.Introduction,
                'Achievements': profile.Achievements,
            }
        elif not profile.IfRecruit:
            response = {
                'ClubName': profile.ClubName,
                'ShezhangName': profile.ShezhangName,
                'ShezhangQq': profile.ShezhangQq,
                'ShezhangGrade': profile.ShezhangGrade,
                'ShezhangClass': profile.ShezhangClass,
                'IfRecruit': 'False',
                'EnrollGroupQq': profile.EnrollGroupQq,
                'Email': profile.Email,
                'Label': profile.Label,
                'State': profile.State,
                'Stars': profile.Stars,
                'Introduction': profile.Introduction,
                'Achievements': profile.Achievements,
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
def club_profile_submit(request):
    try:
        body = json.loads(request.body)
        token = body['Token']
        clubid = body['clubid']
        if(token_authenticate(user_id=clubid,token=token)):
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
                club_object = Club.objects.get(ClubId=clubid)
                club_object.ClubName = clubname
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


@require_http_methods(["POST"])
def event_submit(request):
    pass


@require_http_methods(["POST"])
def event_list(request):
    pass


@require_http_methods(["POST"])
def club_page(request):
    pass


@require_http_methods(["POST"])
def club_page_setting(request):
    pass


@require_http_methods(['POST'])
def cd_file_upload(request):
    try:
        file = request.FILES
        body = json.loads(request.body)
        token = body['CDToken']

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
def club_file_upload(request):
    try:
        file = request.FILES
        body = json.loads(request.body)
        token = body['CDToken']

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
def club_file_download(request):
    try:
        pass
    except:
        pass


@require_http_methods(['POST'])
def cd_file_download(request):
    pass
